# Random Forests — Mathematics, Geometry, Bagging & Variance Reduction

> This chapter is **math-complete first**, intuition-rich second.  
> Nothing is skipped: probability, bias–variance, geometry, and algorithmic details are all included.

---

## 1. Why Decision Trees Need Fixing (Formal Restatement)

From the Decision Tree chapter:

- A single tree estimator \( \hat f(x) \) has:
  - Very low bias
  - Very high variance

Formally:

\[ \text{Var}(\hat f(x)) \text{ is large} \]

Small perturbations in data → different splits → different regions.

Goal of Random Forest:

> Reduce variance **without significantly increasing bias**.

---

## 2. Core Idea of Random Forests (One Sentence)

> **Average many high-variance, low-bias models that are weakly correlated.**

Everything else is implementation detail.

---

## 3. Bagging (Bootstrap Aggregating) — Mathematical Setup

Given dataset:

\[ D = \{(x_i, y_i)\}_{i=1}^n \]

Construct B bootstrap datasets:

\[ D^{(b)} = \{(x_i^{(b)}, y_i^{(b)})\}_{i=1}^n \]

Each dataset is sampled **with replacement**.

Train a tree on each:

\[ \hat f_b(x) \]

Aggregate:

- Regression:
\[ \hat f_{RF}(x) = \frac{1}{B} \sum_{b=1}^B \hat f_b(x) \]

- Classification:
\[ \hat f_{RF}(x) = \text{majority vote}\{\hat f_b(x)\} \]

---

## 4. Why Averaging Reduces Variance (Key Derivation)

Assume:
- Each tree has variance \( \sigma^2 \)
- Pairwise correlation \( \rho \)

Variance of average:

\[ \text{Var}(\bar f) = \rho \sigma^2 + \frac{1-\rho}{B} \sigma^2 \]

As B → ∞:

\[ \text{Var}(\bar f) \to \rho \sigma^2 \]

### Critical insight:
- Variance reduction is **limited by correlation**
- Averaging alone is not enough

---

## 5. Why Feature Randomness Is Necessary

If all trees see:
- Same dominant feature

Then:
- Trees become highly correlated
- \( \rho \approx 1 \)
- Averaging gives little benefit

Random Forest introduces:

> **Feature subsampling at each split**.

---

## 6. Feature Subsampling (Formal Definition)

At each split:
- Randomly sample m features from d
- Find best split among those m

Typically:

\[ m = \sqrt{d} \] (classification)
\[ m = d/3 \] (regression)

This forces:
- Different trees
- Different geometries
- Lower correlation

---

## 7. Geometry of Random Forests

Single tree:
- Axis-aligned rectangles

Forest:
- Union of many partitions
- Averaged piecewise-constant functions

Result:
- Decision boundary becomes **smooth in expectation**
- Still non-parametric

Mathematically:

\[ f_{RF}(x) = \mathbb{E}_{\text{tree}}[f(x)] \]

---

## 8. Bias–Variance Decomposition (Formal)

For Random Forest:

- Bias: slightly higher than single tree
- Variance: dramatically lower

Net effect:

\[ \text{Error}_{RF} < \text{Error}_{Tree} \]

Almost always in practice.

---

## 9. Why Random Forests Rarely Overfit

As B increases:
- Variance decreases
- Bias stays bounded

So:
- Test error stabilizes
- Overfitting is rare

Exception:
- Extremely noisy labels

---

## 10. Out-of-Bag (OOB) Error — Why It Works

Each bootstrap sample leaves out ~36.8% data.

For a point xᵢ:
- Predict using trees that did not see xᵢ

This gives:

\[ \text{OOB Error} \approx \text{Test Error} \]

No validation set needed.

---

## 11. Random Forest for Regression (Math Detail)

Prediction:

\[ \hat y(x) = \frac{1}{B} \sum_b \bar y_{R_b(x)} \]

Where:
- R_b(x) is leaf region in tree b

This is a **kernel-like estimator**.

---

## 12. Random Forest for Classification

Each tree estimates:

\[ P_b(y=k|x) \]

Forest probability:

\[ P(y=k|x) = \frac{1}{B} \sum_b P_b(y=k|x) \]

This explains:
- Better calibration than single trees

---

## 13. Consistency (Theoretical Result)

Under mild assumptions:

\[ \hat f_{RF}(x) \to f(x) \]

As:
- n → ∞
- B → ∞

Random Forests are **statistically consistent**.

---

## 14. Limitations of Random Forests

- Axis-aligned bias remains
- Poor extrapolation
- Large memory footprint
- Less interpretable than single trees

---

## 15. Comparison Summary

| Model | Bias | Variance | Geometry |
|------|------|----------|----------|
| Tree | Low | Very High | Rectangles |
| RF | Slightly ↑ | Very Low | Averaged rectangles |
| Linear | High | Low | Hyperplanes |

---

## 16. Intuition Recap (For Non-Statistical Readers)

- Trees are smart but unstable
- Forests average many opinions
- Randomness makes opinions independent
- Independence makes averaging powerful

---

## 17. Bridge Forward

Random Forest fixes **variance**.

Next:
- **Boosting fixes bias**
- Trees become weak on purpose

---

*Next chapter: Boosting — AdaBoost → Gradient Boosting → XGBoost (math + geometry).*