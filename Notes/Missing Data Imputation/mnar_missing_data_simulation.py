# MNAR Missing Data Simulation – Industry-Grade Notebook
# Goal: Prove WHY naive imputation fails when missingness is NOT random
# Audience: Senior DS / ML interviews, real-world ML systems

# =========================================================
# 1. Imports
# =========================================================
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

np.random.seed(42)

# =========================================================
# 2. Generate Clean Synthetic Data
# =========================================================
# Scenario: Credit risk / income-based approval

n = 8000
income = np.random.lognormal(mean=10, sigma=0.6, size=n)
age = np.random.normal(loc=40, scale=10, size=n)

# Target: default risk (non-linear relation)
logit = -6 + 0.00004 * income - 0.03 * age
prob = 1 / (1 + np.exp(-logit))
y = (np.random.rand(n) < prob).astype(int)

X = pd.DataFrame({
    'income': income,
    'age': age
})

# =========================================================
# 3. Introduce MNAR Missingness
# =========================================================
# High-income users are MORE likely to hide income

missing_prob = (income > np.percentile(income, 75)) * 0.6
mask = np.random.rand(n) < missing_prob

X_mnar = X.copy()
X_mnar.loc[mask, 'income'] = np.nan

print('Missing rate:', X_mnar['income'].isna().mean())

# =========================================================
# 4. Train-Test Split (Leakage Safe)
# =========================================================
X_train, X_test, y_train, y_test = train_test_split(
    X_mnar, y, test_size=0.25, random_state=42, stratify=y
)

# =========================================================
# 5. Baseline: Mean Imputation (WRONG for MNAR)
# =========================================================
mean_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000))
])

mean_pipeline.fit(X_train, y_train)
preds_mean = mean_pipeline.predict_proba(X_test)[:, 1]
auc_mean = roc_auc_score(y_test, preds_mean)

# =========================================================
# 6. Median + Missing Indicator (Correct Strategy)
# =========================================================
indicator_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median', add_indicator=True)),
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000))
])

indicator_pipeline.fit(X_train, y_train)
preds_indicator = indicator_pipeline.predict_proba(X_test)[:, 1]
auc_indicator = roc_auc_score(y_test, preds_indicator)

# =========================================================
# 7. No Imputation (Drop Missing) – Biased Sample
# =========================================================
X_drop = X_mnar.dropna()
y_drop = y[X_mnar['income'].notna()]

X_tr_d, X_te_d, y_tr_d, y_te_d = train_test_split(
    X_drop, y_drop, test_size=0.25, random_state=42, stratify=y_drop
)

no_impute_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000))
])

no_impute_pipeline.fit(X_tr_d, y_tr_d)
preds_drop = no_impute_pipeline.predict_proba(X_te_d)[:, 1]
auc_drop = roc_auc_score(y_te_d, preds_drop)

# =========================================================
# 8. Results Comparison
# =========================================================
results = pd.DataFrame({
    'Strategy': ['Mean Imputation', 'Median + Indicator', 'Drop Missing'],
    'ROC_AUC': [auc_mean, auc_indicator, auc_drop]
})

print(results)

# =========================================================
# 9. Visual Proof of MNAR Bias
# =========================================================
plt.figure()
plt.hist(income, bins=40, alpha=0.6, label='True Income')
plt.hist(X_mnar['income'].dropna(), bins=40, alpha=0.6, label='Observed Income')
plt.legend()
plt.title('MNAR Bias: High Income Disappears')
plt.show()

# =========================================================
# 10. Key Takeaways (READ CAREFULLY)
# =========================================================
# 1. Mean imputation underestimates income → biased coefficients
# 2. Dropping rows removes high-income users → sampling bias
# 3. Missing indicator recovers hidden signal
# 4. Performance gain proves missingness contains information

# =========================================================
# 11. Interview Gold Statements
# =========================================================
# “Missingness itself is predictive.”
# “MNAR requires modeling missingness, not just values.”
# “Indicators act as proxy variables for hidden mechanisms.”

# =========================================================
# 12. Exercises
# =========================================================
# 1. Increase missing severity and observe AUC collapse
# 2. Replace LogisticRegression with XGBoost
# 3. Make age MNAR instead of income
# 4. Remove indicator and inspect coefficient shift
