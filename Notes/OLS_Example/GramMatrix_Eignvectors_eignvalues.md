# Gram Matrix, Eigenvectors, Projection, Correlation & Noise  
*A complete intuition-first walkthrough (no PCA)*

---

## 1. Data and the Design Matrix

We start with raw data.

Suppose we have:
- $n$ data points
- $d$ features

We arrange the data into a **design matrix**:

$X \in \mathbb{R}^{n \times d}$

- Rows represent **data points**
- Columns represent **features**

Each row is a point in **feature space**.

At this stage:
- No transformations
- No directions
- Just the geometric shape of data

---

## 2. Why Do We Compute the Gram Matrix $X^\top X$?

We compute the **Gram matrix**:

$G = X^\top X$

---

### What the Gram matrix represents

- It is **not new data**
- It is a **summary of relationships between features**
- It aggregates dot products across all data points

---

### Meaning of entries

- Diagonal entries $G_{ii}$  
  → total energy / variance of feature $i$

- Off-diagonal entries $G_{ij}$  
  → how much feature $i$ and feature $j$ move together  
  → correlation / redundancy

Important:
- The Gram matrix **does not give directions**
- It only encodes **relationships**

---

## 3. Why the Gram Matrix Is Special

The Gram matrix has two guaranteed properties:

### Symmetry
$G^\top = G$

### Positive semi-definite
$v^\top G v = \|Xv\|^2 \ge 0$

---

### Consequences (Spectral Theorem)

Because of these properties:

- All eigenvalues are **real**
- A **complete set of eigenvectors exists**
- Eigenvectors can be chosen **orthogonal**
- They span the entire feature space

This guarantee **never fails** for Gram matrices.

---

## 4. Eigenvectors — Definition and Meaning

### Mathematical definition

A non-zero vector $v$ is an eigenvector of $G$ if:

$Gv = \lambda v$

where $\lambda$ is the eigenvalue.

---

### Intuitive meaning

An eigenvector is:

> A **direction in feature space** along which the matrix acts as **pure scaling**

- Direction does not rotate
- Only magnitude changes
- No mixing with other directions

Eigenvectors are **not original features**.

---

## 5. Eigenvectors as Linear Combinations of Features

If we have two features $X_1, X_2$, an eigenvector

$v = [a, b]$

represents the direction:

$aX_1 + bX_2$

---

### Interpretation of signs

- $+aX_1 + bX_2$ → features increase together  
- $+aX_1 - bX_2$ → one feature increases, the other decreases  

Eigenvectors encode **relative feature movement**, not individual feature importance.

---

## 6. What Does “Projection Onto a Direction” Mean?

Projection answers:

> “How much of a data point lies along this direction?”

For a data point $x_i$ and a unit vector $\hat v$:

$z_i = x_i \cdot \hat v$

This is simply a **dot product**.

After projection:
- Each data point becomes a scalar
- Scalars show how spread out data is along that direction

---

## 7. Variance Along a Direction

Variance along a direction means:

> The spread of projected values along that direction

- Large spread → important direction
- Small spread → weak direction

---

## 8. Eigenvalues = Variance After Projection

For the Gram matrix $X^\top X$:

> The eigenvalue corresponding to an eigenvector equals the **variance of data when projected onto that direction**

- Large eigenvalue → strong signal
- Small eigenvalue → weak signal
- Zero eigenvalue → no variation (redundant direction)

Eigenvalues measure **strength**, not existence.

---

## 9. Correlation Patterns and Geometry

Correlation determines the **shape of data in feature space**, which directly determines eigenvectors and eigenvalues.

---

### 9.1 Completely Positively Correlated Features

If:

$X_2 = c X_1$

- Data lies on a single straight line
- One dominant eigenvalue
- One eigenvalue $\approx 0$

Interpretation:
- Direction $[1,1]$ has all variance
- Direction $[1,-1]$ has no variance
- Data lies in a 1D subspace

---

### 9.2 Completely Negatively Correlated Features

If:

$X_2 = -c X_1$

- Data lies on a straight line with negative slope
- Eigenvector $[1,-1]$ dominates
- Eigenvector $[1,1]$ has zero variance

Still rank-1 data.

---

### 9.3 Partially Correlated Features

- Data forms an elongated ellipse
- One large eigenvalue
- One smaller eigenvalue

Interpretation:
- Major axis = strong direction
- Minor axis = weaker direction
- Both directions exist, but unequally important

---

### 9.4 Uncorrelated Features

- Data forms a roughly circular cloud
- Eigenvalues are approximately equal

Interpretation:
- No preferred direction
- Any orthogonal basis is valid
- Eigenvectors are not unique

---

## 10. Repeated Eigenvalues

If an eigenvalue has multiplicity $k$:

- The eigenspace is $k$-dimensional
- Eigenvectors are **not unique**
- Any orthonormal basis inside that subspace is valid

Equal eigenvalues mean:
- No dominant direction
- Isotropic variation

---

## 11. Small Eigenvalues Do NOT Mean No Directions

Important clarification:

- Directions always exist for symmetric matrices
- Small eigenvalues mean **little signal**
- Data may simply be tightly clustered

---

## 12. Noise — A Critical Intuition

### Key assumption

> **Noise is approximately equally distributed in all directions**

Noise:
- Has no preferred axis
- Appears isotropic
- Exists everywhere in feature space

---

## 13. Why Do We Divide by Eigenvalues?

Projection alone is harmless.

The question is:
**Why do many methods divide by eigenvalues (or $\sqrt{\lambda}$)?**

---

### 13.1 What We Have After Projection

After projection onto eigenvector $v_j$:

$z_{ij} = x_i \cdot v_j$

These are coordinates in the eigenvector basis.

---

### 13.2 What an Eigenvalue Represents

For $X^\top X$:

$\lambda_j = \text{Var}(z_{ij})$

Eigenvalues encode the **natural scale** of each direction.

---

### 13.3 Why We Normalize Directions

Many algorithms want:

> Each direction to be treated **equally**, independent of scale

So we normalize variance.

---

### 13.4 Where Division Comes From

To make variance equal to 1:

$\tilde z_{ij} = \frac{z_{ij}}{\sqrt{\lambda_j}}$

Then:

$\text{Var}(\tilde z_{ij}) = 1$

This is why we divide by $\sqrt{\lambda_j}$.

---

## 14. Why Small Eigenvalues Amplify Noise

Noise exists in all directions.

If $\lambda_j$ is small:
- Signal variance is small
- Noise variance is comparable

After scaling:

$\tilde z_{ij} = \frac{z_{ij}}{\sqrt{\lambda_j}}$

- $\sqrt{\lambda_j}$ is tiny
- Noise gets magnified
- Noise dominates signal

---

## 15. Why This Is Dangerous

Dividing by small eigenvalues:
- Artificially magnifies meaningless directions
- Causes instability
- Leads to overfitting and numerical issues

---

## 16. Complete Flow (No PCA)

1. Data → design matrix $X$  
2. Gram matrix $X^\top X$ summarizes relationships  
3. Eigenvectors define orthogonal directions  
4. Eigenvalues measure variance  
5. Projection = dot product  
6. Correlation determines geometry  
7. Noise dominates small-eigenvalue directions  

---

## ⭐ Final Master Intuition

> Eigenvectors of the Gram matrix are orthogonal combinations of features defining independent directions of variation; eigenvalues quantify signal strength along those directions; correlation determines geometry; and because noise is spread in all directions, dividing by small eigenvalues amplifies noise and destabilizes learning.
