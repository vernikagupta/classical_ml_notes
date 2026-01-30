# Regularization, Gradients, and Why LASSO Produces Exact Zeros  
*(Complete End-to-End Explanation: Theory → Optimization → Numbers → Elastic Net)*

This document explains **how regularization works mathematically and algorithmically**, focusing on **gradients and residuals**, not geometry.

---

## 1. What is a gradient?

> **A gradient is a rate of change.**  
Outside machine learning, it is simply a **slope**.

### Gradient in 1D

If loss depends on one parameter \( w \):

$$
\frac{dL}{dw}
$$

- Positive → increasing \( w \) increases loss  
- Negative → increasing \( w \) decreases loss  
- Zero → no further improvement possible  

### Gradient in multiple dimensions

For parameters $\( (w_1, w_2, \dots, w_p) \)$:

$$
\nabla L =
\left(
\frac{\partial L}{\partial w_1},
\frac{\partial L}{\partial w_2},
\dots
\right)
$$

Each component answers:  
> “If I change this weight slightly, how does loss change?”

---

## 2. Critical clarification: what optimization is really doing

❌ Optimization does **not** try to make loss zero  
✅ Optimization tries to make the **total gradient zero**

$$
\boxed{
\nabla \text{Total Loss} = 0
}
$$

Loss itself may be non-zero.  
Training stops when **no direction reduces it further**.

---

## 3. Loss + regularization = total objective

$$
\text{Total Loss}(w)
=
\text{Data Loss}(w)
+
\text{Penalty}(w)
$$


$$
\nabla \text{Total Loss}
=
\nabla \text{Data Loss}
+
\nabla \text{Penalty}
$$


---

## 4. What is “gradient kill”?

> **Gradient kill** happens when the gradient from regularization exactly cancels the gradient from the data loss, making the total gradient zero.

- Data wants to move the weight  
- Penalty applies equal opposite force  
- Net gradient = 0 → parameter freezes  

---

## 5. L1 regularization (LASSO)

### Objective

$$
\min_w
\;
\frac{1}{2}\|y - Xw\|_2^2
+
\lambda \sum_{j=1}^{p} |w_j|
$$

### L1 penalty gradient

For \( w_j \neq 0 \):

$$
\frac{d}{dw_j}(\lambda |w_j|)
=
\lambda \cdot \text{sign}(w_j)
$$

At \( w_j = 0 \), derivative does not exist.  
We use a **subgradient**:

$$
\partial(\lambda |w_j|) = [-\lambda, +\lambda]
$$

---

## 6. Linear model and residual

$$
\hat y = Xw = \sum_{k=1}^{p} x_k w_k
$$

Residual:

$$
r = y - Xw
$$

Residual = **what the model has not explained yet**.

---

## 7. Data loss and key derivation

$$
\text{Data Loss}(w)
=
\frac{1}{2}\|y - Xw\|_2^2
=
\frac{1}{2} r^T r
$$

Using the chain rule:

$$
\frac{\partial \text{Data Loss}}{\partial w_j}
=
r^T(-x_j)
=
- x_j^T r
- $$

---

## 8. What is an inner product?

For vectors \( a, b \in \mathbb{R}^n \):

$$
a^T b = \sum_{i=1}^{n} a_i b_i
$$

It measures **alignment**.  
If vectors are standardized:

$$
a^T b \propto \text{correlation}(a, b)
$$

---

## 9. How optimization works with multiple features

Optimization repeatedly:
1. Computes residual  
2. Checks each feature’s correlation with residual  
3. Kills or keeps the feature  
4. Updates residual  
5. Repeats until total gradient is zero  

---

## 10. Why weak and correlated features disappear

If:

$$
|x_j^T r| \le \lambda
\Rightarrow
w_j = 0
$$

This is **gradient kill**.

---

## 11. Why L2 (Ridge) does not produce zeros

$$
\lambda w_j^2
\Rightarrow
\frac{d}{dw_j} = 2\lambda w_j
$$

At \( w_j = 0 \): penalty gradient = 0 → no cancellation.

---

## 12. Summary table

| Aspect | L1 (LASSO) | L2 (Ridge) |
|---|---|---|
| Data gradient | \(x_j^T r\) | \(x_j^T r\) |
| Penalty at 0 | \([−\lambda, +\lambda]\) | 0 |
| Gradient kill | Yes | No |
| Exact zeros | Yes | No |

---

## 13. Pseudocode (Coordinate Descent)

```text
Initialize w = 0, r = y
Repeat:
  for each feature j:
    r = r + x_j * w_j
    g_j = x_jᵀ r
    if |g_j| ≤ λ:
        w_j = 0
    else:
        w_j = (g_j − sign(g_j)·λ) / (x_jᵀ x_j)
    r = r − x_j * w_j
```
---

## 14. Numeric walkthrough

Dataset:
x1,x2,y  
1,1,3  
1,0,2  
0,1,1  

With \( \lambda = 1 \).  
Step-by-step updates show how features survive or get killed as residual changes.

---

## 15. Extension to Elastic Net

Objective:

$$
\min_w
\;
\frac{1}{2}\|y - Xw\|^2
+
\lambda_1 \sum_j |w_j|
+
\lambda_2 \sum_j w_j^2
$$

Elastic Net:
- L1 → sparsity  
- L2 → stability  

Update:

$$
w_j =
\frac{\text{SoftThreshold}(x_j^T r, \lambda_1)}
{x_j^T x_j + 2\lambda_2}
$$

---

## 16. Final takeaway

> **Regularization is about how gradients interact with residuals during optimization.  
L1 kills weak gradients, L2 shrinks strong ones, Elastic Net does both.**
