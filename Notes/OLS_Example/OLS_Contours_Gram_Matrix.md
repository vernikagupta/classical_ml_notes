# OLS Loss Contours and the Gram Matrix (Step-by-Step)

This note shows **how the ellipse-shaped loss contours arise** in linear regression and **how they come directly from the Gram matrix** \(X^T X\).  
This is written so you can follow it **line by line with pen and paper**.

---

## 1. Start from the OLS loss

For linear regression:

\[
L(w) = \frac{1}{2} \| y - Xw \|^2
\]

---

## 2. Expand the loss

Expand the squared norm:

\[
\begin{aligned}
L(w)
&= \frac{1}{2}(y - Xw)^T (y - Xw) \\
&= \frac{1}{2} y^T y - w^T X^T y + \frac{1}{2} w^T X^T X w
\end{aligned}
\]

---

## 3. Identify what controls the *shape*

- \(\frac{1}{2} y^T y\) → constant (does not affect geometry)
- \(- w^T X^T y\) → shifts the minimum
- \(\frac{1}{2} w^T X^T X w\) → **controls curvature and shape**

👉 **Contours depend only on the quadratic term**

So for contours, we study:

\[
\boxed{
w^T X^T X w = c
}
\]

---

## 4. The Gram matrix

For our smallest example:

\[
X^T X =
\begin{bmatrix}
2 & 1 \\
1 & 2
\end{bmatrix}
\]

This is the **Gram matrix**:
- diagonal → feature strength
- off-diagonal → feature overlap

---

## 5. Write the parameter vector

\[
w =
\begin{bmatrix}
w_1 \\
w_2
\end{bmatrix}
\]

---

## 6. Compute the quadratic form

\[
w^T (X^T X) w
=
\begin{bmatrix}
w_1 & w_2
\end{bmatrix}
\begin{bmatrix}
2 & 1 \\
1 & 2
\end{bmatrix}
\begin{bmatrix}
w_1 \\
w_2
\end{bmatrix}
\]

First multiplication:

\[
\begin{bmatrix}
2 & 1 \\
1 & 2
\end{bmatrix}
\begin{bmatrix}
w_1 \\
w_2
\end{bmatrix}
=
\begin{bmatrix}
2w_1 + w_2 \\
w_1 + 2w_2
\end{bmatrix}
\]

Second multiplication:

\[
\begin{aligned}
w^T X^T X w
&= w_1(2w_1 + w_2) + w_2(w_1 + 2w_2) \\
&= 2w_1^2 + 2w_1 w_2 + 2w_2^2
\end{aligned}
\]

---

## 7. The contour equation (ellipse)

\[
\boxed{
2w_1^2 + 2w_1 w_2 + 2w_2^2 = c
}
\]

This is the **equation of an ellipse** in parameter space.

- Different values of \(c\) give different contours
- Smaller \(c\) → closer to minimum
- Larger \(c\) → higher loss

---

## 8. Why it is not a circle

- The cross-term \(w_1 w_2\) tilts the ellipse
- Unequal curvature in different directions
- This comes from **feature correlation**

---

## 9. Eigenvectors explain the axes

Eigen-decomposition:

\[
X^T X = Q \Lambda Q^T
\]

- Columns of \(Q\) → **principal directions**
- Diagonal of \(\Lambda\) → **curvature along those directions**

In eigen-coordinates \(z = Q^T w\):

\[
\lambda_1 z_1^2 + \lambda_2 z_2^2 = c
\]

This is an **axis-aligned ellipse**.

---

## 10. Geometric interpretation

- Gram matrix \(X^T X\) defines the **geometry of the loss surface**
- Eigenvectors = **axes of the ellipse**
- Eigenvalues = **how steep or flat the loss is**

---

## 11. One-sentence takeaway

> **The OLS loss surface is a quadratic bowl whose contours are ellipses defined by \(w^T (X^T X) w = c\); the Gram matrix shapes the bowl, and its eigenvectors give the principal directions of curvature.**
