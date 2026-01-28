# 🧩 Missing Data Imputation – Industry-Grade ML Guide

This repository is a **deep, production-oriented guide to missing data handling in Machine Learning**.

It goes far beyond *"fill with mean"* and focuses on:

* **Why data is missing**
* **How missingness biases models**
* **Which imputation strategy works in which scenario**
* **How missing data behaves in trees, time-series, and production systems**
* **How to monitor and retrain safely in MLOps**

This repo is designed for:

* Data Scientists (mid → senior)
* Machine Learning Engineers
* Interview preparation (real decision-making questions)
* Production ML systems

---

## 📂 Repository Structure

```
Missing Data Imputation/
├── missing_data/
│   ├── README.md
│   ├── missing_data_imputation.md
│   ├── missing_data_imputation_playground.ipynb
│   ├── MNAR_missing_data_simulation.ipynb
│   ├── Tree_Based_Models_Missing_Values.ipynb
│   ├── Time_Series_Missing_Data_Imputation.ipynb
│   └── MLOps_Monitoring_Missing_Data.ipynb
```

Each notebook builds **conceptually and practically** on the previous one.

---

## 🧠 Learning Philosophy

> **Missing data handling is a modeling decision, not a preprocessing step.**

This repo emphasizes:

* Data-generating processes (MCAR / MAR / MNAR)
* Bias, variance, and signal loss
* Model-aware preprocessing
* Production safety and monitoring

Every notebook answers **three questions**:

1. *Why does this method work?*
2. *When does it fail?*
3. *How does this impact real models?*

---

## 📘 Notebook Guide (Read in Order)

### 1️⃣ `missing_data_imputation.md`

**Theory + decision framework**

Covers:

* MCAR / MAR / MNAR with industry examples
* Method selection matrix
* Advantages, limitations, and failure modes
* Interview-ready reasoning

📌 *Start here for conceptual grounding.*

---

### 2️⃣ `missing_data_imputation_playground.ipynb`

**Real dataset + pipelines**

* Dataset: UCI Adult Income
* Leakage-safe train/test split
* Mean vs Median+Indicator vs KNN
* ROC-AUC comparison

📌 *Shows how imputation choices affect real model performance.*

---

### 3️⃣ `MNAR_missing_data_simulation.ipynb`

**Most important notebook in this repo** ⭐

* Explicit MNAR simulation
* Why mean imputation silently fails
* Why dropping rows creates bias
* How missing indicators recover signal
* Visual + metric proof

📌 *This notebook alone differentiates senior candidates.*

---

### 4️⃣ `Tree_Based_Models_Missing_Values.ipynb`

**Trees are different — but not magic**

* Native missing handling in trees
* Mean vs native vs indicator comparison
* Overfitting via missing paths
* Regularization rules

📌 *Explains how XGBoost / LightGBM actually treat missing values.*

---

### 5️⃣ `Time_Series_Missing_Data_Imputation.ipynb`

**Forecasting & sensor data pitfalls**

* Random gaps vs sensor outages
* Forward fill, backward fill, interpolation
* Regime-change smoothing failures
* Leakage risks in time-series

📌 *Critical for forecasting, ops, and GenAI pipelines.*

---

### 6️⃣ `MLOps_Monitoring_Missing_Data.ipynb`

**Production & monitoring (Staff-level)**

* Missingness drift = data drift
* Indicator feature monitoring
* AUC decay detection
* Alerting & retraining triggers
* Imputer retraining strategy

📌 *Moves from notebooks to real ML systems.*

---

## 🛠️ Tech Stack

* Python
* NumPy, Pandas
* scikit-learn
* Matplotlib

All notebooks are **runnable locally or on Google Colab**.

---

## 🎯 Interview Readiness

After completing this repo, you should confidently answer:

* *How do you detect MNAR in practice?*
* *Why did adding a missing indicator improve AUC?*
* *Do trees really not need imputation?*
* *How do you monitor missing data in production?*
* *Do you retrain imputers? Why?*

---

## 🚨 Common Industry Mistakes (Addressed Here)

❌ Imputing before train-test split
❌ Using target to impute features
❌ Ignoring missingness drift
❌ Assuming trees solve everything
❌ Interpolating across regime changes

This repo explicitly shows **why these fail**.

---

## ✅ How to Use This Repo

1. Read `missing_data_imputation.md`
2. Run notebooks **in order**
3. Modify simulations (severity, drift, gaps)
4. Observe metric changes
5. Treat missingness as a modeling signal

---

## 📌 Final Takeaway

> **If you don’t understand why data is missing, you don’t understand your model.**

This repository teaches you to reason about missing data the way **experienced ML practitioners do**.

---

⭐ If this repo helped you, consider starring it or extending it with:

* Outliers
* Encoding failures
* Feature scaling & leakage
* End-to-end preprocessing pipelines

