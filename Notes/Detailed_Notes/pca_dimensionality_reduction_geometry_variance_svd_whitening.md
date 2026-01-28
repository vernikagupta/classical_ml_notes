# PCA & Dimensionality Reduction — Geometry, Variance, SVD & Whitening

> This chapter is **math-complete** and **geometry-first**.  
> Every formula is derived or motivated; intuition is layered at the end so non-statistical readers can still follow.

---

## 1. Why Dimensionality Reduction Exists (Problem Statement)

High-dimensional data causes:
- Redundancy (correlated features)
- Noise accumulation
- Ill-conditioned matrices (e.g., XᵀX)
- Poor generalization and slow learning

Goal:

> Represent data with **fewer dimensions** while **preserving information**.

---

## 2. Formal Setup & Centering (Non-Negotiable)

Given data matrix:

X ∈ ℝⁿˣᵈ

Center features:

X_c = X − 1·μᵀ

Where μ is the column-wise mean.

Why centering matters:
- PCA studies **variance around the mean**
- Without centering, first component points toward mean

---

## 3. Variance of a Projection (Key Quantity)

Project data onto a unit vector w:

z = X_c w

Variance of projection:

Var(z) = (1/n) ||X_c w||² = wᵀ S w

Where covariance matrix:

S = (1/n) X_cᵀ X_c

---

## 4. PCA Optimization Problem (Exact)

First principal component:

maximize   wᵀ S w
subject to ||w|| = 1

This is a **Rayleigh quotient**.

Solution:
- w = eigenvector of S with largest eigenvalue

---

## 5. Eigenvalues, Eigenvectors & Geometry

Eigen-decomposition:

S = Q Λ Qᵀ

- Eigenvectors → directions
- Eigenvalues → variance along those directions

Geometric meaning:
- PCA rotates coordinate axes
- Aligns them with maximum spread

---

## 6. Multiple Components (Orthogonality Constraint)

For k components:

maximize   Tr(Wᵀ S W)
subject to WᵀW = I

Solution:
- Columns of W = top k eigenvectors

Orthogonality ensures:
- No duplicated information

---

## 7. Reconstruction View (Dual Perspective)

Low-dimensional representation:

Z = X_c W

Reconstruction:

\hat X = Z Wᵀ

PCA minimizes:

||X_c − \hat X||²_F

Among all rank-k linear reconstructions.

---

## 8. PCA as Best Rank-k Approximation (Theorem)

(Eckart–Young–Mirsky)

PCA gives the **optimal** rank-k approximation in Frobenius norm.

This is a **global optimum**, not heuristic.

---

## 9. SVD Connection (Practically Important)

SVD of centered data:

X_c = U Σ Vᵀ

Then:
- Columns of V = principal directions
- Σ² / n = eigenvalues of covariance

SVD avoids explicit S computation.

---

## 10. PCA vs Linear Regression Geometry

- Linear regression: project y onto Col(X)
- PCA: project X onto dominant subspace

Both are **orthogonal projections**, but:
- Regression uses y
- PCA ignores y (unsupervised)

---

## 11. Whitening (Variance Normalization)

Whitened data:

X_white = X_c V Λ^{-1/2}

Properties:
- Covariance = I
- Features uncorrelated and unit variance

Used in:
- Optimization
- ICA
- Neural networks

---

## 12. When PCA Helps (And When It Hurts)

Helps when:
- Strong correlations
- Noise in low-variance directions

Hurts when:
- Target depends on low-variance directions
- Nonlinear structure dominates

PCA preserves variance, **not labels**.

---

## 13. Kernel PCA (Conceptual Extension)

Idea:
- Apply PCA in feature space φ(x)

Use kernel matrix:

K = Φ Φᵀ

Eigen-decompose K instead of S.

Captures:
- Nonlinear manifolds

---

## 14. PCA & SVM Connection

Kernel PCA:
- Learns directions in RKHS

Kernel SVM:
- Finds max-margin separator in same space

Both rely on:
- Eigen-structure of kernel matrix

---

## 15. Bias–Variance View

Reducing dimension:
- Increases bias
- Reduces variance

PCA trades:
- Simplicity for stability

---

## 16. Intuition Recap (Non-Statistical Reader)

- PCA finds directions with most spread
- Rotates data to remove redundancy
- Keeps the “important” directions

Think:
> Compressing data without losing shape

---

## 17. Unified Mental Model

- Variance = information
- Eigenvectors = directions
- Eigenvalues = strength
- PCA = rotate + drop weak axes

---

## 18. Where PCA Fits in ML Pipelines

- Preprocessing before regression/SVM
- Visualization (2D/3D)
- Denoising
- Speeding up learning

---

*Next: ICA, LDA, t-SNE & UMAP — different notions of “importance”.*

