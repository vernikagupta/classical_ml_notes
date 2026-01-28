# Classical Machine Learning — Geometry, Probability & Optimization

> This repository is a **conceptually complete, math-heavy guide to Classical Machine Learning**.
> It is written to build *true understanding* — not just usage — by unifying:
>
> * **Geometry** (spaces, projections, margins)
> * **Probability** (uncertainty, likelihoods, latent variables)
> * **Optimization** (loss surfaces, convexity, EM, gradients)
>
> Every topic is explained **from first principles**, with intuition layered *after* formal math.

---

## 🎯 Who This Repository Is For

* Data Scientists who want **deep foundations**
* ML Engineers preparing for **serious interviews**
* Researchers who want **clean conceptual structure**
* Non-statistical engineers who want intuition *without losing rigor*

If you are looking for quick recipes, this is **not** the right place.

---

## 🧠 How to Study This Repository (Very Important)

This repository is **order-sensitive**.
Each chapter builds concepts used later.

Below is the **recommended study order**, with *why* each block exists.

---

## 📘 PART 1 — Linear Models & Geometry Foundations

### 1️⃣ Linear Regression

📂 `linear-regression/`

**Why first**:

* Introduces vectors, projections, loss surfaces
* Builds geometric intuition for all ML

**You learn**:

* Least squares geometry
* Bias–variance
* Conditioning & ill-posed problems

---

### 2️⃣ Logistic Regression & Softmax

📂 `logistic-regression/`

**Why next**:

* Extends linear geometry to probabilities
* Introduces likelihood & cross-entropy

**You learn**:

* Log-odds
* Convex optimization
* Decision boundaries

---

## 📘 PART 2 — Margin-Based Learning

### 3️⃣ Support Vector Machines (SVM)

📂 `svm/`

**Why here**:

* Shifts from probability to pure geometry
* Introduces margins & duality

**You learn**:

* Convex optimization
* Kernel trick
* Capacity control

---

## 📘 PART 3 — Tree-Based Models & Ensembles

### 4️⃣ Decision Trees

📂 `decision-trees/`

**Why now**:

* Breaks linear geometry
* Introduces axis-aligned partitions

---

### 5️⃣ Random Forests

📂 `random-forests/`

**Why next**:

* Introduces variance reduction by averaging

---

### 6️⃣ Boosting (AdaBoost → GBM)

📂 `boosting/`

**Why next**:

* Introduces bias reduction
* Functional gradient descent

---

### 7️⃣ XGBoost, LightGBM & CatBoost

📂 `xgboost/`, `lightgbm-catboost/`

**Why here**:

* Shows industrial-strength boosting
* Explicit regularization & second-order geometry

---

## 📘 PART 4 — Dimensionality Reduction & Representation

### 8️⃣ PCA

📂 `pca/`

**Why now**:

* Introduces eigenvalues & subspaces
* Foundation for kernels & latent variables

---

### 9️⃣ LDA, ICA & Kernel PCA

📂 `lda-ica-kernelpca/`

**Why next**:

* Shows different meanings of “important direction”

---

### 🔟 Manifold Learning (t-SNE & UMAP)

📂 `manifold-learning/`

**Why after PCA**:

* Handles nonlinear structure
* Visualization & topology

---

## 📘 PART 5 — Probabilistic Models & Latent Variables

### 1️⃣1️⃣ Bayesian Decision Theory & Naive Bayes

📂 `bayesian-methods/`

**Why here**:

* Formalizes uncertainty & optimal decisions

---

### 1️⃣2️⃣ Gaussian Mixture Models & EM

📂 `bayesian-methods/`

**Why last**:

* Combines probability, geometry, optimization
* Bridge to deep generative models

---

## 🔁 Optional Reading Orders

### 🔹 Interview-Oriented Path

1. Linear Regression
2. Logistic Regression
3. SVM
4. Decision Trees
5. Random Forests
6. XGBoost

---

### 🔹 Probability-First Path

1. Bayesian Decision Theory
2. Naive Bayes
3. GMM & EM
4. PCA / PPCA

---

## 🧩 How This Connects to Deep Learning

This repository prepares you for:

* Backpropagation (from gradient boosting)
* VAEs (from PPCA & GMMs)
* Representation learning (from PCA & kernels)

Deep learning **extends**, not replaces, this foundation.

---

## ✨ Final Advice

* Do **not rush**
* Re-derive equations on paper
* Visualize geometry wherever possible
* Revisit earlier chapters often

If you truly understand this repository,
**modern ML will feel natural, not magical**.

---

Happy learning 🌱
