# Missing Data Imputation – Runnable Playground Notebook
# Dataset: UCI Adult Income (Real Industry-Style Dataset)

# This notebook is designed to be run locally or on Colab.
# It demonstrates how different imputation strategies affect real model performance.

# =========================================================
# 1. Imports
# =========================================================
import numpy as np
import pandas as pd

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# =========================================================
# 2. Load Real Dataset (Adult Income)
# =========================================================
# Industry relevance:
# - Income prediction (finance / risk)
# - Naturally missing values marked as '?'

adult = fetch_openml('adult', version=2, as_frame=True)
X = adult.data
y = (adult.target == '>50K').astype(int)

# Replace '?' with NaN
X = X.replace('?', np.nan)

# =========================================================
# 3. Train-Test Split (CRITICAL)
# =========================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# =========================================================
# 4. Identify Feature Types
# =========================================================
num_features = X.select_dtypes(include=['int64', 'float64']).columns
cat_features = X.select_dtypes(include=['object']).columns

# =========================================================
# 5. Baseline: Mean / Mode Imputation
# =========================================================n
numeric_pipeline_mean = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_pipeline_mode = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor_mean = ColumnTransformer([
    ('num', numeric_pipeline_mean, num_features),
    ('cat', categorical_pipeline_mode, cat_features)
])

model_mean = Pipeline([
    ('preprocess', preprocessor_mean),
    ('model', LogisticRegression(max_iter=1000))
])

model_mean.fit(X_train, y_train)
preds_mean = model_mean.predict_proba(X_test)[:, 1]
auc_mean = roc_auc_score(y_test, preds_mean)

print('AUC – Mean/Mode Imputation:', auc_mean)

# =========================================================
# 6. Median + Missing Indicator (Production Preferred)
# =========================================================

numeric_pipeline_indicator = Pipeline([
    ('imputer', SimpleImputer(strategy='median', add_indicator=True)),
    ('scaler', StandardScaler())
])

preprocessor_indicator = ColumnTransformer([
    ('num', numeric_pipeline_indicator, num_features),
    ('cat', categorical_pipeline_mode, cat_features)
])

model_indicator = Pipeline([
    ('preprocess', preprocessor_indicator),
    ('model', LogisticRegression(max_iter=1000))
])

model_indicator.fit(X_train, y_train)
preds_indicator = model_indicator.predict_proba(X_test)[:, 1]
auc_indicator = roc_auc_score(y_test, preds_indicator)

print('AUC – Median + Indicator:', auc_indicator)

# =========================================================
# 7. KNN Imputation (Numeric Only)
# =========================================================

numeric_pipeline_knn = Pipeline([
    ('imputer', KNNImputer(n_neighbors=5)),
    ('scaler', StandardScaler())
])

preprocessor_knn = ColumnTransformer([
    ('num', numeric_pipeline_knn, num_features),
    ('cat', categorical_pipeline_mode, cat_features)
])

model_knn = Pipeline([
    ('preprocess', preprocessor_knn),
    ('model', LogisticRegression(max_iter=1000))
])

model_knn.fit(X_train, y_train)
preds_knn = model_knn.predict_proba(X_test)[:, 1]
auc_knn = roc_auc_score(y_test, preds_knn)

print('AUC – KNN Imputation:', auc_knn)

# =========================================================
# 8. Comparison Summary
# =========================================================
results = pd.DataFrame({
    'Method': ['Mean/Mode', 'Median + Indicator', 'KNN'],
    'ROC_AUC': [auc_mean, auc_indicator, auc_knn]
})

print('\nImputation Strategy Comparison')
print(results)

# =========================================================
# 9. Key Observations (Read This)
# =========================================================
# - Indicator often improves performance → MNAR signal
# - KNN may help but is slower and sensitive to scaling
# - Simple methods + indicators are often best in production

# =========================================================
# 10. Exercises
# =========================================================
# 1. Drop indicator and observe AUC change
# 2. Switch LogisticRegression → XGBoost / LightGBM
# 3. Artificially create MNAR and re-test
# 4. Track missing % drift over time
