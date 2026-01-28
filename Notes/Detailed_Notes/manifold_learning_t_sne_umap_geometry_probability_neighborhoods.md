# Manifold Learning — t-SNE & UMAP (Geometry, Probability & Neighborhoods)

> This chapter explains **why PCA/LDA fail on manifolds** and how **t-SNE and UMAP** solve a *different* problem.
> Math is explicit. Intuition is layered so non-statistical readers can follow.

---

## 1. Why Linear Methods Fail on Manifolds

Assumption behind PCA/LDA:
- Data lies near a **linear subspace**

Reality:
- Data often lies on **curved manifolds**
  - Images
  - Text embeddings
  - Human motion

Linear projection:
- Tears apart curved neighborhoods

Goal of manifold learning:

> Preserve **local neighborhood structure**, not global variance.

---

## 2. What Manifold Learning Optimizes (Key Shift)

Dimensionality reduction objectives differ:

| Method | Preserves |
|------|----------|
| PCA | Global variance |
| LDA | Class separation |
| t-SNE | Local similarity |
| UMAP | Topological structure |

Manifold learning is **not** about reconstruction error.

---

# PART I — t-SNE

---

## 3. High-Dimensional Similarities (Exact Definition)

For points x_i, x_j:

p_{j|i} = exp(-||x_i-x_j||² / 2σ_i²) / ∑_{k≠i} exp(-||x_i-x_k||² / 2σ_i²)

σ_i chosen via **perplexity**.

Joint probability:

p_{ij} = (p_{j|i}+p_{i|j}) / 2n

---

## 4. Low-Dimensional Similarities

In low-d space (y_i):

q_{ij} = (1 + ||y_i-y_j||²)⁻¹ / ∑_{k≠l} (1 + ||y_k-y_l||²)⁻¹

Uses **Student-t distribution**.

Why heavy tails:
- Prevents crowding

---

## 5. Objective Function (KL Divergence)

Minimize:

KL(P || Q) = ∑ p_{ij} log(p_{ij}/q_{ij})

Interpretation:
- Preserve neighbors
- Allow distant points to move freely

---

## 6. Geometry of t-SNE

- Strong attraction between neighbors
- Weak repulsion globally

Result:
- Clear clusters
- Distorted global distances

---

## 7. Limitations of t-SNE

- No parametric mapping
- Poor global structure
- Sensitive to hyperparameters

t-SNE is a **visualization tool**, not embedding model.

---

# PART II — UMAP

---

## 8. Mathematical Foundation of UMAP

UMAP is based on:
- Riemannian geometry
- Algebraic topology

Key assumption:

> Data lies on a manifold with uniform local connectivity.

---

## 9. Fuzzy Simplicial Sets (Core Idea)

Construct a weighted graph:

w_{ij} = exp(-(d(x_i,x_j)-ρ_i)/σ_i)

This defines a **fuzzy topological structure**.

---

## 10. Low-Dimensional Optimization

UMAP minimizes:

Cross-entropy between high-d and low-d graphs

Attractive + repulsive forces balance.

---

## 11. Geometry of UMAP

- Preserves both local and some global structure
- More faithful inter-cluster distances

UMAP embeddings are more **stable** than t-SNE.

---

## 12. Comparison: t-SNE vs UMAP

| Aspect | t-SNE | UMAP |
|------|-------|------|
| Objective | KL divergence | Cross-entropy |
| Global structure | Poor | Better |
| Speed | Slow | Fast |
| Parametric | No | Yes |

---

## 13. When to Use What

- Visualization → t-SNE
- Representation + viz → UMAP
- Preprocessing → PCA/UMAP combo

---

## 14. Intuition Recap (Non-Statistical Reader)

- t-SNE pulls neighbors together
- UMAP preserves shape of neighborhoods
- Neither preserves distances exactly

---

*This chapter completes manifold learning foundations.*

