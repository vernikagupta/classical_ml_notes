# Missing Data Imputation – Industry-Level Notebook

> **Goal**: This notebook-style markdown explains *how missing data occurs in real industry projects*, *how to diagnose it*, *which imputation method to use and when*, *why methods fail*, and *how these choices impact ML models*.  
Designed to be **GitHub-ready**, **interview-ready**, and **production-aware**.

---

## 1. Why Missing Data Is Not a “Preprocessing Detail”

In real projects, missing data is often:
- A **signal**, not a bug
- Caused by **business logic**, not randomness
- **Correlated with the target** (very dangerous)

Examples:
- Credit score missing because user is new → high risk
- Salary missing because user chose not to disclose → sensitive signal
- Sensor missing because system failed → operational risk

> ❗ Treating all missing values with `mean()` can silently destroy model performance.

---

## 2. Types of Missingness (Critical for Method Selection)

### 2.1 MCAR – Missing Completely At Random
Missingness is independent of both features and target.

Example:
- Random packet loss in telemetry
- Data corruption during logging

Effect:
- Dataset remains unbiased

Safe methods:
- Mean / Median / Mode

---

### 2.2 MAR – Missing At Random
Missingness depends on **other observed variables**, not on itself.

Example:
- Income missing mostly for students
- Age missing for users from a specific country

Effect:
- Bias exists but is explainable

Safe methods:
- Group-based imputation
- Regression / KNN

---

### 2.3 MNAR – Missing Not At Random (Most Dangerous)
Missingness depends on the **value itself**.

Example:
- High income users hide income
- Sick patients skip medical tests

Effect:
- Severe bias if ignored

Safe methods:
- Missing indicators
- Domain-driven constants
- Model-based handling (trees)

---

## 3. Industry Mapping: Missingness → Solution

| Industry | Feature | Missing Reason | Recommended Strategy |
|--------|--------|---------------|----------------------|
| Finance | Income | User hides | Missing flag + median |
| Healthcare | Test result | Test not done | Separate category |
| E-commerce | Ratings | New product | Zero + indicator |
| Sensors | Temperature | Device failure | Interpolation |
| HR | Salary | Confidential | Model-based |

---

## 4. Baseline Imputation Methods (With Failure Modes)

### 4.1 Mean Imputation

**Use when**:
- MCAR
- Symmetric distribution

**Why it works**:
- Minimizes squared error

**Why it fails**:
- Reduces variance
- Destroys correlation
- Biases linear models

Example:
```python
X['age'] = X['age'].fillna(X['age'].mean())
```

---

### 4.2 Median Imputation

**Use when**:
- Skewed data
- Outliers present

**Why better than mean**:
- Robust to extreme values

**Limitation**:
- Still ignores feature relationships

---

### 4.3 Mode Imputation (Categorical)

**Use when**:
- One category dominates

**Failure**:
- Artificially inflates majority class

---

## 5. Constant / Domain-Driven Imputation

Example:
- `salary = -1`
- `rating = 0`

**Use when**:
- Missingness itself is meaningful

**Always add indicator**:
```python
X['salary_missing'] = X['salary'].isna().astype(int)
X['salary'] = X['salary'].fillna(-1)
```

**Common mistake**:
- Using constant without indicator

---

## 6. Missing Indicator (Extremely Important)

> Trees, boosting, and neural nets can *learn missingness patterns*.

**When to use**:
- MNAR
- Business-driven missingness

**Risk**:
- Indicator may overfit in small datasets

---

## 7. Group-Based Imputation (Industry Favorite)

Example:
- Fill income by (education, job level)

```python
X['income'] = X.groupby('job_level')['income'].transform(
    lambda x: x.fillna(x.median())
)
```

**Why it works**:
- Preserves conditional distribution

**Fails when**:
- Groups are too small

---

## 8. Regression Imputation

Predict missing feature using other features.

Steps:
1. Split rows where value exists
2. Train regression
3. Predict missing rows

**Pros**:
- Preserves relationships

**Cons**:
- Overconfident predictions
- Leakage if target is used

---

## 9. KNN Imputation

```python
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=5)
X_imputed = imputer.fit_transform(X)
```

**Use when**:
- Features are correlated
- Distance metric makes sense

**Fails when**:
- High dimensional data
- Mixed scale features (must scale first)

---

## 10. Iterative / MICE Imputation (Advanced)

```python
from sklearn.impute import IterativeImputer
```

**Idea**:
- Each feature is predicted using others iteratively

**Pros**:
- Strong statistical grounding

**Cons**:
- Slow
- Assumes MAR

---

## 11. Time-Series Specific Imputation

### Methods
- Forward fill
- Backward fill
- Linear interpolation
- Seasonal interpolation

```python
X['value'] = X['value'].interpolate(method='linear')
```

**Failure**:
- Regime changes
- Long gaps

---

## 12. Tree-Based Models: Special Case

Models like:
- XGBoost
- LightGBM
- CatBoost

Can **natively handle missing values**.

**But**:
- Still benefit from indicators
- Missing path may overfit

---

## 13. Impact on Different Models

| Model | Sensitivity |
|-----|------------|
| Linear Regression | Very high |
| Logistic Regression | High |
| KNN | Extreme |
| SVM | High |
| Tree-based | Low |
| Neural Networks | Medium |

---

## 14. Common Industry Mistakes

❌ Impute before train-test split  
❌ Use target to impute features  
❌ Ignore missingness pattern  
❌ Use same strategy for all features

---

## 15. Interview Decision Framework

**Ask these questions**:
1. Why is the data missing?
2. Is missingness correlated with target?
3. Is model linear or tree-based?
4. Is interpretability required?

---

## 16. Mini Playground Notebook (Try Yourself)

Tasks:
1. Create MNAR data
2. Compare:
   - Mean
   - Median + Indicator
   - KNN
3. Train Logistic Regression
4. Compare AUC

---

## 17. Final Cheat Sheet

| Scenario | Best Choice |
|--------|-------------|
| Random missing | Mean / Median |
| Business-driven | Constant + Indicator |
| Correlated features | KNN / MICE |
| Time series | Interpolation |
| Trees | Native handling + indicator |

---

## 18. Production Checklist for Missing Data Imputation

This section reflects **real ML production systems**, not notebooks.

---

### 18.1 Before Imputation (Data Understanding)

✅ Identify **why** data is missing (MCAR / MAR / MNAR)  
✅ Check missingness correlation with target  
✅ Visualize missingness matrix (`missingno`, heatmaps)  
✅ Talk to domain / business teams

❌ Never assume missing = random

---

### 18.2 Train–Test Safety (Leakage Prevention)

✅ Split train / validation / test **before imputation**  
✅ Fit imputers **only on training data**  
✅ Reuse fitted imputers for validation & test

❌ Never compute mean/median on full dataset

---

### 18.3 Feature-Level Strategy (Not One-Size-Fits-All)

For each feature, document:
- Missing reason
- Chosen method
- Justification

Example:
- `income`: MNAR → median + indicator  
- `age`: MCAR → median  
- `salary_band`: MAR → group-based

---

### 18.4 Indicators in Production

✅ Add missing indicators for:
- MNAR features
- Business-driven missingness

⚠️ Monitor indicator importance
- Sudden spike → upstream data issue

---

### 18.5 Model-Aware Decisions

| Model | Production Rule |
|------|----------------|
| Linear / Logistic | Careful imputation + scaling |
| KNN | Impute + scale first |
| Trees | Native missing + indicators |
| Neural Nets | Explicit imputation required |

---

### 18.6 Pipeline Implementation (Mandatory)

✅ Use `Pipeline` / `ColumnTransformer`  
✅ Keep imputation inside model pipeline  
✅ Version control imputers

❌ No ad-hoc `fillna()` outside pipeline

---

### 18.7 Monitoring After Deployment

Track over time:
- Missing value % per feature
- Indicator feature drift
- Model performance vs missing rate

Example alerts:
- Missing % ↑ suddenly → data ingestion failure
- Indicator importance ↑ → behavior shift

---

### 18.8 Retraining & Backfilling Rules

✅ Refit imputers during retraining  
✅ Do NOT backfill historical data blindly  
✅ Respect temporal order for time-series

---

### 18.9 Documentation (Often Ignored, Very Important)

Each feature should have:
- Missing reason
- Imputation logic
- Owner (data source)

This saves months during audits & model debugging.

---

### 18.10 Final Production Red Flags

🚨 If any of these occur, stop the pipeline:
- Missingness pattern changes abruptly
- New category of missing appears
- Indicator dominates feature importance

---

## 19. Key Takeaway

> **Missing data handling is a modeling decision, not a preprocessing step.**

A strong data scientist explains **why** a method was chosen — not just *how*.

---

If you want, next we can:
- Convert this into a **Jupyter notebook with experiments**
- Add **real datasets (Kaggle / UCI)**
- Add **interview Q&A** for missing data

