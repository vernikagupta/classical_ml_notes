# MLOps & Monitoring for Missing Data – Production Notebook
# Goal: Detect missingness drift, prevent silent model decay, and trigger retraining
# Audience: ML Engineers, Senior Data Scientists, Production Owners

# =========================================================
# 1. Imports
# =========================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

np.random.seed(42)

# =========================================================
# 2. Simulated Production Dataset (Daily Batches)
# =========================================================
# Scenario: Credit / risk scoring system with incoming batches

n_days = 60
rows_per_day = 300

all_batches = []

for day in range(n_days):
    income = np.random.lognormal(mean=10, sigma=0.6, size=rows_per_day)
    age = np.random.normal(40, 10, rows_per_day)

    # Gradual MNAR drift: more users hide income over time
    missing_prob = 0.1 + 0.005 * day
    mask = (np.random.rand(rows_per_day) < missing_prob)
    income[mask] = np.nan

    logit = -6 + 0.00005 * np.nan_to_num(income, nan=0) - 0.03 * age
    prob = 1 / (1 + np.exp(-logit))
    y = (np.random.rand(rows_per_day) < prob).astype(int)

    batch = pd.DataFrame({
        'day': day,
        'income': income,
        'age': age,
        'target': y
    })

    all_batches.append(batch)

prod_data = pd.concat(all_batches).reset_index(drop=True)

# =========================================================
# 3. Baseline Training (Day 0–10)
# =========================================================
train_data = prod_data[prod_data['day'] <= 10]

X_train = train_data[['income', 'age']]
y_train = train_data['target']

pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median', add_indicator=True)),
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train, y_train)

# =========================================================
# 4. Monitor Missingness Drift Over Time
# =========================================================
missing_rate = prod_data.groupby('day')['income'].apply(lambda x: x.isna().mean())

plt.figure()
plt.plot(missing_rate)
plt.xlabel('Day')
plt.ylabel('Missing Rate (Income)')
plt.title('Missingness Drift in Production')
plt.show()

# =========================================================
# 5. Monitor Model Performance Degradation
# =========================================================
auc_by_day = []

days = sorted(prod_data['day'].unique())
for day in days:
    batch = prod_data[prod_data['day'] == day]
    X_batch = batch[['income', 'age']]
    y_batch = batch['target']

    preds = pipeline.predict_proba(X_batch)[:, 1]
    auc = roc_auc_score(y_batch, preds)
    auc_by_day.append(auc)

plt.figure()
plt.plot(days, auc_by_day)
plt.xlabel('Day')
plt.ylabel('ROC-AUC')
plt.title('Model Performance Decay Due to Missing Drift')
plt.show()

# =========================================================
# 6. Indicator Feature Monitoring
# =========================================================
# Missing indicator index
indicator_index = pipeline.named_steps['imputer'].indicator_.features_

print('Indicator index for income:', indicator_index)

# =========================================================
# 7. Production Alert Rules
# =========================================================
# Example thresholds
MISSING_ALERT = 0.3
AUC_ALERT = 0.6

alerts = []

for day, mr, auc in zip(days, missing_rate, auc_by_day):
    if mr > MISSING_ALERT:
        alerts.append((day, 'Missing Rate Spike'))
    if auc < AUC_ALERT:
        alerts.append((day, 'AUC Degradation'))

print('Alerts Triggered:')
for alert in alerts[:5]:
    print(alert)

# =========================================================
# 8. Retraining Strategy
# =========================================================
# Retrain when either:
# - Missingness crosses threshold
# - AUC drops persistently

retrain_data = prod_data[prod_data['day'] <= 30]

X_retrain = retrain_data[['income', 'age']]
y_retrain = retrain_data['target']

pipeline.fit(X_retrain, y_retrain)

# =========================================================
# 9. Key Production Principles (READ CAREFULLY)
# =========================================================
# 1. Missingness drift is data drift
# 2. Indicators are monitoring signals
# 3. Retrain imputers with models
# 4. Alerts must be automated

# =========================================================
# 10. Interview-Ready Statements
# =========================================================
# “I monitor missingness as a first-class drift signal.”
# “Imputers are retrained, not frozen.”
# “Indicators act as early warning sensors.”

# =========================================================
# 11. Exercises
# =========================================================
# 1. Add PSI for missing indicators
# 2. Monitor feature distribution drift
# 3. Add rolling window retraining
# 4. Simulate sudden ingestion failure
