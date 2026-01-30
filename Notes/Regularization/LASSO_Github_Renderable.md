# Regularization, Gradients, and Why LASSO Produces Exact Zeros
*(GitHub-renderable version — no manual changes needed)*

---

## 1. What is a gradient?

### Gradient in 1D

$$
\frac{dL}{dw}
$$

### Gradient in multiple dimensions

$$
\nabla L =
\begin{pmatrix}
\frac{\partial L}{\partial w_1} \\
\frac{\partial L}{\partial w_2} \\
\vdots \\
\frac{\partial L}{\partial w_p}
\end{pmatrix}
$$

---

## 2. Critical clarification: what optimization is really doing

$$
\nabla \text{Total Loss} = 0
$$

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

## 5. L1 regularization (LASSO)

### Objective

$$
\min_w \;
\frac{1}{2}\lVert y - Xw \rVert_2^2
+
\lambda \sum_{j=1}^{p} |w_j|
$$

### L1 penalty gradient (non-zero)

$$
\frac{d}{dw_j}(\lambda |w_j|)
=
\lambda \cdot \text{sign}(w_j)
$$

### Subgradient at zero

$$
\partial(\lambda |w_j|)
=
[-\lambda, +\lambda]
$$

---

## 6. Linear model and residual

$$
\hat y = Xw = \sum_{k=1}^{p} x_k w_k
$$

$$
r = y - Xw
$$

---

## 7. Data loss and gradient

$$
\text{Data Loss}(w)
=
\frac{1}{2}\lVert y - Xw \rVert_2^2
=
\frac{1}{2} r^T r
$$

$$
\frac{\partial \text{Data Loss}}{\partial w_j}
=
- x_j^T r
$$

---

## 8. Inner product

$$
a^T b = \sum_{i=1}^{n} a_i b_i
$$

---

## 10. Gradient kill condition

$$
|x_j^T r| \le \lambda
\quad \Rightarrow \quad
w_j = 0
$$

---

## 11. Ridge penalty gradient

$$
\lambda w_j^2
\Rightarrow
\frac{d}{dw_j} = 2\lambda w_j
$$

---

## 15. Elastic Net

### Objective

$$
\min_w \;
\frac{1}{2}\lVert y - Xw \rVert^2
+
\lambda_1 \sum_j |w_j|
+
\lambda_2 \sum_j w_j^2
$$

### Update rule

$$
w_j =
\frac{
\text{SoftThreshold}(x_j^T r, \lambda_1)
}{
x_j^T x_j + 2\lambda_2
}
$$

---

## Final takeaway

**L1 kills weak gradients, L2 shrinks strong ones, Elastic Net does both.**
