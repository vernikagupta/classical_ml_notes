# Regularization — Mathematical Derivation (Ridge, Lasso, ElasticNet)

This chapter derives **why regularization works mathematically**. We will start from Linear Regression and see exactly **what changes in the equations**, **why solutions become stable**, and **why some penalties create sparsity**.

> Read this as a story: problem → math → consequence.

---

## Q1. What problem appears in the OLS normal equation?

**What:**  
The OLS solution is:
β̂ = (XᵀX)⁻¹ Xᵀy

**Why this fails:**  
- XᵀX can be singular or ill-conditioned
- Small eigenvalues → huge variance in β̂

**Consequence:**  
Coefficients become unstable.

---

## Q2. How does Ridge Regression modify the optimization problem?

**What:**  
Ridge adds an L2 penalty to OLS.

**How (math):**  
Minimize:
||y − Xβ||² + λ||β||²

**Why:**  
To discourage large coefficients.

---

## Q3. How does Ridge change the normal equation?

**Derivation:**  
Take gradient and set to zero:

XᵀXβ + λβ = Xᵀy

**Solution:**  
β̂_ridge = (XᵀX + λI)⁻¹ Xᵀy

---

## Q4. Why does adding λI fix singularity?

**Why:**  
XᵀX + λI shifts all eigenvalues by λ.

**Interpretation:**  
Flat directions gain curvature.

**Result:**  
Matrix becomes invertible.

---

## Q5. How does Ridge reduce variance mathematically?

**Eigenvalue view:**  
Small eigenvalues are inflated by λ.

**Effect:**  
Coefficient variance is reduced in unstable directions.

---

## Q6. Why does Ridge not produce exact zeros?

**Why:**  
The L2 penalty is smooth and differentiable.

**Consequence:**  
Weights are shrunk but rarely hit zero.

---

## Q7. What happens to Ridge solution as λ → 0?

**Result:**  
Ridge → OLS.

---

## Q8. What happens as λ → ∞?

**Result:**  
β̂ → 0.

**Interpretation:**  
Model ignores features.

---

## Q9. Why does Lasso have no closed-form solution?

**What:**  
Lasso uses L1 penalty:
λ Σ |βᵢ|

**Why:**  
Absolute value is not differentiable at zero.

---

## Q10. How is Lasso optimized then?

**Methods:**  
- Coordinate descent
- Subgradient methods

**Key idea:**  
Optimize one coefficient at a time.

---

## Q11. Why does Lasso drive coefficients exactly to zero?

**Math intuition:**  
The subgradient allows zero to be an optimal point.

**Effect:**  
Automatic feature selection.

---

## Q12. What is the bias–variance tradeoff for Lasso?

**Bias:**  
Higher than Ridge.

**Variance:**  
Lower when irrelevant features exist.

---

## Q13. When does Lasso become unstable?

**Why:**  
With highly correlated features.

**Effect:**  
Randomly selects one feature and drops others.

---

## Q14. How does ElasticNet combine L1 and L2?

**What:**  
ElasticNet penalty:
λ₁||β||₁ + λ₂||β||²

**Why:**  
- L1 → sparsity
- L2 → stability

---

## Q15. Why does ElasticNet work better with correlated features?

**Why:**  
L2 term encourages grouped selection.

**Interpretation:**  
Correlated features survive together.

---

## Q16. How does regularization affect gradient descent?

**Effect:**  
Adds an extra gradient term:

∂/∂β (λ||β||²) = 2λβ

**Result:**  
Weights are continuously pulled toward zero.

---

## Q17. Is regularization equivalent to adding noise?

**Yes (conceptually):**  
Ridge ≈ Gaussian noise in inputs.

**Why:**  
Noise discourages reliance on exact values.

---

## Q18. What is the Bayesian interpretation of Ridge?

**View:**  
Ridge = MAP estimation with Gaussian prior on β.

**Interpretation:**  
We believe coefficients should be small.

---

## Q19. What is the Bayesian view of Lasso?

**View:**  
Lasso = MAP with Laplace prior.

**Effect:**  
Sharp peak at zero → sparsity.

---

## Q20. Mathematical takeaway

- Ridge stabilizes solutions
- Lasso selects features
- ElasticNet balances both

All three modify the **geometry of the solution space**, not the data.

---

📌 **Next:** Geometric interpretation — circles, diamonds, corners, and why sparsity emerges.