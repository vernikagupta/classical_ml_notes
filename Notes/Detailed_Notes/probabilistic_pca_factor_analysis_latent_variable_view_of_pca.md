# Probabilistic PCA & Factor Analysis — Latent Variable View of PCA

> This chapter reframes PCA as a **probabilistic latent-variable model**, connecting
> PCA ↔ Gaussian models ↔ EM algorithm ↔ modern representation learning.

---

## 1. Why Deterministic PCA Is Incomplete

Standard PCA:
- Algebraic
- Geometric
- No explicit noise model

Questions PCA cannot answer:
- How much variance is noise?
- How to generate new data?
- How to compare models probabilistically?

---

## 2. Latent Variable Model (Formal)

Assume:

z ∼ 𝒩(0, I_k)

Observed data:

x = W z + μ + ε

Noise:

ε ∼ 𝒩(0, σ² I)

This is **Probabilistic PCA (PPCA)**.

---

## 3. Likelihood Function

Marginal distribution:

x ∼ 𝒩(μ, C)

Where:

C = W Wᵀ + σ² I

---

## 4. Maximum Likelihood Solution

ML estimate of W:

W = U_k (Λ_k − σ² I)^{1/2} R

Where:
- U_k = top eigenvectors of covariance
- Λ_k = corresponding eigenvalues
- R = arbitrary rotation

As σ² → 0:
- PPCA → PCA

---

## 5. EM Algorithm for PPCA

### E-step

Compute:

E[z|x]

### M-step

Update W and σ²

EM provides:
- Stable estimation
- Missing-data handling

---

## 6. Geometry of PPCA

- Latent space is Gaussian
- Observed space is noisy projection

PCA axes emerge as:
- ML directions under Gaussian noise

---

## 7. Factor Analysis (Generalization)

FA relaxes isotropic noise:

ε ∼ 𝒩(0, Ψ)

Where Ψ is diagonal but not scalar.

FA models:
- Feature-specific noise

---

## 8. PCA vs PPCA vs FA

| Aspect | PCA | PPCA | FA |
|------|-----|------|----|
| Noise model | None | Isotropic | Diagonal |
| Probabilistic | No | Yes | Yes |
| Missing data | No | Yes | Yes |

---

## 9. Connection to EM & Deep Models

- PPCA is linear VAE
- FA is probabilistic encoder

Modern deep generative models generalize this.

---

## 10. Intuition Recap (Non-Statistical Reader)

- PCA finds directions
- PPCA explains data generation
- FA separates signal and noise

---

*This chapter bridges classical PCA to modern latent-variable models.*

