# Regularization — Geometric Interpretation (Why Ridge Shrinks & Lasso Selects)

This chapter explains **regularization visually and geometrically**. Once this clicks, you will *never* forget why Ridge shrinks, Lasso selects, and ElasticNet balances both.

> Geometry explains regularization better than equations.

---

## Q1. What geometric problem is Linear Regression solving?

**What:**  
Linear Regression minimizes squared error.

**Geometry:**  
We are finding the point where **elliptical loss contours** touch the feasible region.

**Mental image:**  
Imagine concentric ellipses expanding outward from the minimum.

---

## Q2. How does regularization change this picture?

**What:**  
Regularization adds a **constraint region** on the coefficients.

**Instead of:**  
Searching everywhere,

**We now:**  
Search only inside a bounded region.

---

## Q3. What does Ridge (L2) constraint look like?

**Geometry:**  
A **circle (or sphere)** centered at the origin.

**Math:**  
||β||² ≤ c

**Interpretation:**  
All directions are penalized smoothly and equally.

---

## Q4. Why does Ridge shrink coefficients smoothly?

**Why:**  
The circular boundary has no sharp corners.

**Effect:**  
The solution almost never lies exactly on an axis.

**Result:**  
Coefficients become small, but not zero.

---

## Q5. What does Lasso (L1) constraint look like?

**Geometry:**  
A **diamond (in 2D)** or polytope (in higher dimensions).

**Math:**  
Σ |βᵢ| ≤ c

---

## Q6. Why does Lasso produce sparse solutions?

**Key reason:**  
The diamond has **sharp corners on the axes**.

**Optimization behavior:**  
Ellipses are likely to hit a corner.

**Result:**  
One or more coefficients become exactly zero.

---

## Q7. Why is sparsity useful?

**Benefits:**  
- Feature selection
- Simpler models
- Easier interpretation

**Cost:**  
Higher bias.

---

## Q8. Why does Lasso struggle with correlated features?

**Geometry:**  
Multiple axes point in similar directions.

**Effect:**  
Lasso arbitrarily chooses one corner.

**Result:**  
Unstable feature selection.

---

## Q9. What does ElasticNet constraint look like?

**Geometry:**  
A **rounded diamond**.

**Combination:**  
- L1 → corners
- L2 → smoothness

---

## Q10. Why does ElasticNet work better in practice?

**Why:**  
- Retains sparsity
- Stabilizes correlated features

**Interpretation:**  
Groups of correlated features survive together.

---

## Q11. How does λ change geometry?

**What:**  
λ controls size of constraint region.

**Small λ:**  
Large region → behaves like OLS.

**Large λ:**  
Small region → strong shrinkage.

---

## Q12. Why does regularization reduce variance geometrically?

**Why:**  
Limits movement in unstable directions.

**Effect:**  
Prevents solutions from chasing noise directions.

---

## Q13. How does regularization fix multicollinearity visually?

**Problem:**  
Ellipses are very elongated.

**Fix:**  
Regularization rounds them.

**Result:**  
Stable intersection point.

---

## Q14. Why is L2 preferred when interpretation matters?

**Why:**  
All features are retained.

**Interpretation:**  
Coefficient magnitudes are comparable.

---

## Q15. Why is L1 preferred for feature selection?

**Why:**  
It explicitly zeros coefficients.

**Interpretation:**  
Implicit model selection.

---

## Q16. Why is geometry more intuitive than math here?

**Reason:**  
Optimization is about intersections of shapes.

**Once you see the shapes:**  
You can predict behavior without equations.

---

## Q17. Visual references (highly recommended)

- Ridge vs Lasso constraint regions:
https://web.stanford.edu/~hastie/ElemStatLearn/figures/ENetPath.pdf

- Geometric intuition of Lasso:
https://stats.stackexchange.com/questions/137907/why-does-lasso-set-coefficients-to-zero

- Animated Ridge vs Lasso explanation:
https://www.youtube.com/watch?v=NGf0voTMlcs

---

## Q18. Geometric takeaway

- Ridge shrinks because of smooth boundaries
- Lasso selects because of corners
- ElasticNet balances both

Geometry explains everything regularization does.

---

📌 **Next:** Tricky interview questions on regularization (where most people fail).

