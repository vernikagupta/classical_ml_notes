# Tree-Based Models & Missing Values – Industry-Grade Notebook
# Focus: XGBoost / LightGBM / Decision Trees
# Goal: Understand WHY trees handle missing values differently and WHEN they still fail

# =========================================================
# 1. Imports
# =========================================================
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

np.random.seed(42)

# =========================================================
# 2. Synthetic Industry Dataset (Credit Risk)
# =========================================================
# Features:
# - income (MNAR)
# - age (MCAR)

n = 6000
income = np.random.lognormal(mean=10, sigma=0.6, size=n)
age = np.random.normal(40, 10, size=n)

logit = -6 + 0.00005 * income - 0.03 * age
prob = 1 / (1 + np.exp(-logit))
y = (np.random.rand(n) < prob).astype(int)

X = pd.DataFrame({'income': income, 'age': age})

# Introduce MNAR: high income hides income
mask = (income > np.percentile(income, 70)) & (np.random.rand(n) < 0.6)
X.loc[mask, 'income'] = np.nan

print('Missing rate (income):', X['income'].isna().mean())

# =========================================================
# 3. Train-Test Split
# =========================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# =========================================================
# 4. Decision Tree WITHOUT Imputation
# =========================================================
# Trees can route missing values during split

tree_native = DecisionTreeClassifier(
    max_depth=4,
    min_samples_leaf=100,
    random_state=42
)

tree_native.fit(X_train, y_train)
preds_native = tree_native.predict_proba(X_test)[:, 1]
auc_native = roc_auc_score(y_test, preds_native)

# =========================================================
# 5. Decision Tree WITH Mean Imputation
# =========================================================
mean_tree = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('model', DecisionTreeClassifier(
        max_depth=4,
        min_samples_leaf=100,
        random_state=42
    ))
])

mean_tree.fit(X_train, y_train)
preds_mean = mean_tree.predict_proba(X_test)[:, 1]
auc_mean = roc_auc_score(y_test, preds_mean)

# =========================================================
# 6. Decision Tree WITH Median + Indicator
# =========================================================
indicator_tree = Pipeline([
    ('imputer', SimpleImputer(strategy='median', add_indicator=True)),
    ('model', DecisionTreeClassifier(
        max_depth=4,
        min_samples_leaf=100,
        random_state=42
    ))
])

indicator_tree.fit(X_train, y_train)
preds_indicator = indicator_tree.predict_proba(X_test)[:, 1]
auc_indicator = roc_auc_score(y_test, preds_indicator)

# =========================================================
# 7. Compare Results
# =========================================================
results = pd.DataFrame({
    'Strategy': ['Tree Native Missing', 'Tree + Mean', 'Tree + Indicator'],
    'ROC_AUC': [auc_native, auc_mean, auc_indicator]
})

print(results)

# =========================================================
# 8. Why Trees Handle Missing Differently (Conceptual)
# =========================================================
# During split, tree learns:
# - If feature is missing → go left or right
# - Direction chosen to minimize impurity

# Missing is treated as a CATEGORY, not noise

# =========================================================
# 9. When Tree-Based Models FAIL with Missing Values
# =========================================================
# 1. Small datasets → missing path overfits
# 2. High-cardinality missing patterns
# 3. Missing correlated with time (data drift)

# =========================================================
# 10. Production Rules for Trees
# =========================================================
# DO:
# - Add missing indicators for MNAR
# - Monitor missing path splits
# - Regularize depth & leaf size

# DON'T:
# - Assume native handling is always enough
# - Ignore indicator feature importance

# =========================================================
# 11. Interview-Ready Statements
# =========================================================
# “Trees treat missingness as a split decision, not an imputed value.”
# “Indicators still help when missingness is a business signal.”
# “Native handling can overfit without regularization.”

# =========================================================
# 12. Exercises
# =========================================================
# 1. Increase depth and observe overfitting
# 2. Add more MNAR features
# 3. Compare with Logistic Regression
# 4. Replace with XGBoost / LightGBM
