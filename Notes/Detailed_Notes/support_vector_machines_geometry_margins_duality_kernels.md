# Support Vector Machines (SVM) — Geometry, Margins, Duality & Kernels

> This chapter is **math-complete** and **geometry-first**, with intuition layered so a non-statistical engineer can follow *after* the formalism.
> SVMs are best understood as a story about **margins, convex optimization, and geometry in high-dimensional spaces**.

---

## 1. Why SVM Exists (What Linear / Logistic Still Miss)

Linear & Logistic Regression:
- Fit averages or probabilities
- Optimize point-wise losses

But classification often needs:
- **Robust separation**
- **Resistance to outliers**
- **Maximum safety margin** between classes

SVM answers:

> *Among all separating hyperplanes, choose the one with the **largest margin***.

This is a **geometric principle**, not a probabilistic one.

---

## 2. Geometry of a Hyperplane (Formal)

A hyperplane is defined as:

wᵀx + b = 0

Where:
- w is the normal vector
- b is the offset

Decision rule:

ŷ = sign(wᵀx + b)

Distance of a point x from the hyperplane:

|wᵀx + b| / ||w||

This distance formula is central to SVM.

---

## 3. Margin — Exact Mathematical Definition

For binary labels yᵢ ∈ {−1, +1}, impose:

yᵢ (wᵀxᵢ + b) ≥ 1

The **functional margin** is:

yᵢ (wᵀxᵢ + b)

The **geometric margin** is:

yᵢ (wᵀxᵢ + b) / ||w||

SVM maximizes the **minimum geometric margin**.

---

## 4. Hard-Margin SVM (Linearly Separable Case)

### Optimization Problem

Minimize:

1/2 ||w||²

Subject to:

yᵢ (wᵀxᵢ + b) ≥ 1  for all i

Why this objective?
- Margin = 2 / ||w||
- Maximizing margin ⇔ minimizing ||w||²

This is a **convex quadratic program**.

---

## 5. Why Only a Few Points Matter (Support Vectors)

At optimum:
- Most points satisfy constraint strictly
- A few points lie **exactly on the margin**

These are **support vectors**.

Formally:

yᵢ (wᵀxᵢ + b) = 1

Only support vectors determine:
- w
- b

All other points are irrelevant.

---

## 6. Soft-Margin SVM (Real Data Case)

Real data is not perfectly separable.

Introduce slack variables ξᵢ ≥ 0:

yᵢ (wᵀxᵢ + b) ≥ 1 − ξᵢ

Objective:

1/2 ||w||² + C ∑ ξᵢ

Where:
- C controls margin–violation tradeoff

This fixes:
- Noise
- Overlapping classes

---

## 7. Loss Function View (Hinge Loss)

Soft-margin SVM minimizes:

L(y, f(x)) = max(0, 1 − y f(x))

Total objective:

1/2 ||w||² + C ∑ max(0, 1 − yᵢ f(xᵢ))

Why hinge loss?
- Penalizes only margin violations
- Ignores confidently correct points

---

## 8. Primal Problem (Complete Form)

Minimize over w, b, ξ:

1/2 ||w||² + C ∑ ξᵢ

Subject to:
- yᵢ (wᵀxᵢ + b) ≥ 1 − ξᵢ
- ξᵢ ≥ 0

This is convex ⇒ **global optimum guaranteed**.

---

## 9. Dual Formulation (Very Important)

Construct Lagrangian and derive dual:

Maximize:

∑ αᵢ − 1/2 ∑∑ αᵢ αⱼ yᵢ yⱼ (xᵢᵀxⱼ)

Subject to:
- 0 ≤ αᵢ ≤ C
- ∑ αᵢ yᵢ = 0

This is the **dual problem**.

---

## 10. Why Duality Matters (Key Insight)

From KKT conditions:

w = ∑ αᵢ yᵢ xᵢ

Implications:
- Solution is a weighted sum of training points
- Only αᵢ > 0 points matter → support vectors

Also:
- Data appears only as dot products

This unlocks kernels.

---

## 11. Kernel Trick (Formal Statement)

Replace dot product:

xᵢᵀxⱼ → K(xᵢ, xⱼ)

Where:

K(x, z) = φ(x)ᵀ φ(z)

φ maps data to higher-dimensional space **implicitly**.

No need to compute φ(x) explicitly.

---

## 12. Common Kernels (Math + Geometry)

### Linear

K(x,z) = xᵀz

Geometry:
- Same as linear SVM

---

### Polynomial

K(x,z) = (xᵀz + c)^d

Geometry:
- Captures feature interactions
- Curved boundaries

---

### RBF (Gaussian)

K(x,z) = exp(−||x − z||² / (2σ²))

Geometry:
- Infinite-dimensional feature space
- Local influence of points

---

## 13. Geometry of Kernel SVMs

Decision function:

f(x) = ∑ αᵢ yᵢ K(xᵢ, x) + b

Interpretation:
- Each support vector creates a bump
- Boundary is sum of bumps

Highly flexible yet convex.

---

## 14. Why SVMs Generalize Well

Key reasons:
- Margin maximization
- Convex optimization
- Capacity controlled by margin, not dimension

This is called **structural risk minimization**.

---

## 15. Bias–Variance View

- Large margin → low variance
- Kernel choice controls bias

SVM trades:
- Model complexity
- Margin size
n
---

## 16. Multiclass SVM (Brief but Complete)

Approaches:
- One-vs-Rest
- One-vs-One

Each reduces to binary SVMs.

---

## 17. Practical Considerations

- Feature scaling is critical
- Kernel choice dominates performance
- Large datasets → linear SVM or approximations

---

## 18. Intuition Recap (Non-Statistical Reader)

- SVM draws the safest possible boundary
- Only a few critical points matter
- Kernels bend space without explicit mapping

---

## 19. Unified Mental Model

> SVM = Geometry + Convex Optimization + Margins

Not probabilistic.
Not heuristic.

Pure geometry.

---

*Next logical chapter: From SVMs to Neural Networks — margins vs representations.*

