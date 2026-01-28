# XGBoost — Second-Order Boosting, Regularization & Tree Geometry

> This chapter completes the boosting story.  
> It explains **why XGBoost works**, not just *how to use it*.  
> Math is explicit; intuition is layered after.

---

## 1. Why Gradient Boosting Still Needed Improvement

From Gradient Boosting:
- Sequentially reduces bias
- Uses first-order gradients

Problems in practice:
- Overfitting with deep trees
- No explicit control on tree complexity
- Slow convergence
- Instability with noisy gradients

XGBoost fixes these **structurally**, not heuristically.

---

## 2. Core Philosophy of XGBoost

XGBoost is:

> **Regularized, second-order gradient boosting with optimal tree scoring.**

Three key upgrades:
1. Explicit regularization
2. Second-order (Hessian) information
3. Optimal greedy tree construction

---

## 3. Additive Model (Formal Setup)

Prediction at iteration t:

\[ \hat y^{(t)} = \sum_{k=1}^t f_k(x), \quad f_k \in \mathcal{F} \]

Where:
- Each f_k is a decision tree
- \( \mathcal{F} \) is the space of regression trees

---

## 4. Objective Function (Very Important)

XGBoost minimizes:

\[ \mathcal{L}^{(t)} = \sum_i l(y_i, \hat y_i^{(t)}) + \sum_k \Omega(f_k) \]

Regularization term:

\[ \Omega(f) = \gamma T + \frac{1}{2}\lambda \sum_{j=1}^T w_j^2 \]

Where:
- T = number of leaves
- w_j = leaf weights
- γ penalizes tree size
- λ penalizes leaf magnitude

---

## 5. Why Regularization Is Placed on Trees

Instead of regularizing parameters β:
- XGBoost regularizes **function complexity**

Effects:
- Controls overfitting structurally
- Prefers smaller trees
- Prefers smoother predictions

---

## 6. Second-Order Taylor Expansion (Key Math)

At iteration t, expand loss:

\[ l(y, \hat y^{(t-1)} + f(x)) \approx l(y, \hat y^{(t-1)}) + g_i f(x_i) + \frac{1}{2} h_i f(x_i)^2 \]

Where:

\[ g_i = \partial_{\hat y} l(y_i, \hat y^{(t-1)}) \]
\[ h_i = \partial_{\hat y}^2 l(y_i, \hat y^{(t-1)}) \]

This is where **g and h come from**.

---

## 7. Objective Simplification

Dropping constants:

\[ \tilde{\mathcal{L}} = \sum_i [ g_i f(x_i) + \frac{1}{2} h_i f(x_i)^2 ] + \Omega(f) \]

This converts boosting into a **quadratic optimization problem**.

---

## 8. Tree Structure Representation

A tree f maps:

\[ f(x) = w_{q(x)} \]

Where:
- q(x) assigns leaf index
- w_j is leaf score

---

## 9. Optimal Leaf Weight (Exact Solution)

For a leaf j:

\[ G_j = \sum_{i \in j} g_i \]
\[ H_j = \sum_{i \in j} h_i \]

Optimal weight:

\[ w_j^* = - \frac{G_j}{H_j + \lambda} \]

This is a **closed-form solution**.

---

## 10. Optimal Value of a Leaf

Substitute back:

\[ \mathcal{L}_j^* = - \frac{1}{2} \frac{G_j^2}{H_j + \lambda} \]

This gives **leaf quality**.

---

## 11. Split Gain (How Trees Are Grown)

Gain from splitting leaf into L and R:

\[ Gain = \frac{1}{2} \left( \frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{(G_L+G_R)^2}{H_L+H_R+\lambda} \right) - \gamma \]

Split is accepted if:

Gain > 0

---

## 12. Geometry of XGBoost Trees

Each tree:
- Fits **gradient-weighted residuals**
- Curvature-aware (via h)

Regularization:
- Prevents extreme leaf weights
- Penalizes unnecessary splits

Geometrically:
- Boundary bends smoothly
- No violent corrections

---

## 13. Why Second-Order Information Matters

Using h_i:
- Accounts for confidence
- Dampens noisy gradients
- Improves convergence speed

Analogy:
- Gradient → direction
- Hessian → step size confidence

---

## 14. Bias–Variance View

- Boosting reduces bias
- Regularization controls variance

XGBoost balances both explicitly.

---

## 15. Classification Example (Logistic Loss)

For logistic loss:

\[ g_i = \sigma(\hat y_i) - y_i \]
\[ h_i = \sigma(\hat y_i)(1-\sigma(\hat y_i)) \]

These plug directly into gain formulas.

---

## 16. Why XGBoost Is Fast (Conceptual)

- Second-order convergence
- Greedy pruning
- Parallel split finding
- Cache-aware access

Speed is a consequence of math, not tricks.

---

## 17. Why XGBoost Generalizes Well

- Explicit regularization
- Shrinkage (learning rate)
- Tree depth control
- Subsampling

All reduce overfitting geometrically.

---

## 18. Comparison Summary

| Model | Bias | Variance | Regularization |
|------|------|----------|----------------|
| GBM | Low | Medium–High | Implicit |
| XGBoost | Low | Controlled | Explicit |

---

## 19. Intuition Recap (Non-Statistical Reader)

- XGBoost fixes mistakes carefully
- Measures how wrong and how confident
- Penalizes complexity
- Builds strong models safely

---

## 20. Final Mental Model

> XGBoost = Boosting + Curvature + Regularization

It is not magic.
It is **careful mathematics applied to trees**.

---

*This completes the classical tree-based ensemble journey.*

