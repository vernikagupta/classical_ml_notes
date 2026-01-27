# Linear Regression — Mathematical Derivations

This section derives Linear Regression **from first principles**. If this clicks, Logistic Regression, SVMs, and Neural Networks become much easier.

---

## Q1. What is the optimization problem in Linear Regression?

**Answer:**  
Minimize the sum of squared errors.

**Math:**  
L(w) = (1/n) (y − Xw)ᵀ(y − Xw)

---

## Q2. Why do we write Linear Regression in matrix form?

**Answer:**  
It simplifies derivation and reveals geometric structure.

---

## Q3. What is the Normal Equation?

**Answer:**  
Closed-form solution for OLS.

**Math:**  
β̂ = (XᵀX)⁻¹ Xᵀ y

---

## Q4. How do we derive the Normal Equation?

**Answer:**  
By setting gradient of loss w.r.t. β to zero.

---

## Q5. What is the gradient of squared loss?

**Answer:**  
∇β L = −2Xᵀ(y − Xβ)

---

## Q6. Why does setting gradient to zero give minimum?

**Answer:**  
Loss is convex.

---

## Q7. When does the Normal Equation fail?

**Answer:**  
When XᵀX is singular.

---

## Q8. What makes XᵀX singular?

**Answer:**  
Perfect multicollinearity or redundant features.

---

## Q9. What does singularity mean geometrically?

**Answer:**  
Some feature directions collapse.

---

## Q10. Why can’t singular matrices be inverted?

**Answer:**  
They lose information in some dimensions.

---

## Q11. How does pseudoinverse solve this?

**Answer:**  
Inverts only non-zero singular values.

---

## Q12. What is Moore–Penrose pseudoinverse?

**Answer:**  
Generalized inverse using SVD.

---

## Q13. How is OLS solution expressed using pseudoinverse?

**Answer:**  
β̂ = X⁺ y

---

## Q14. Why does multicollinearity inflate variance?

**Answer:**  
Small changes in data cause large coefficient changes.

---

## Q15. Does multicollinearity bias coefficients?

**Answer:**  
No, but increases variance.

---

## Q16. Why does feature scaling not affect OLS solution?

**Answer:**  
OLS solution is scale-invariant.

---

## Q17. Why does feature scaling affect Gradient Descent?

**Answer:**  
It changes curvature of loss surface.

---

## Q18. Gradient Descent vs Normal Equation?

**Answer:**  
Normal Equation: exact but expensive.  
Gradient Descent: approximate but scalable.

---

## Q19. Computational complexity of Normal Equation?

**Answer:**  
O(p³) due to matrix inversion.

---

## Q20. When do we prefer Gradient Descent?

**Answer:**  
High-dimensional or large datasets.

---

## Q21. What is batch Gradient Descent?

**Answer:**  
Uses entire dataset per update.

---

## Q22. What is stochastic Gradient Descent?

**Answer:**  
Uses one sample per update.

---

## Q23. Why does SGD converge faster initially?

**Answer:**  
Noisy gradients escape flat regions.

---

## Q24. Why does SGD fluctuate near minimum?

**Answer:**  
Gradient noise.

---

## Q25. What is learning rate mathematically?

**Answer:**  
Step size in parameter space.

---

## Q26. Why does large learning rate diverge?

**Answer:**  
Overshoots minimum.

---

## Q27. What is Hessian in Linear Regression?

**Answer:**  
H = 2XᵀX

---

## Q28. Why is Hessian constant in Linear Regression?

**Answer:**  
Loss is quadratic.

---

## Q29. What does eigenvalue of Hessian represent?

**Answer:**  
Curvature along a direction.

---

## Q30. Why is Linear Regression convex?

**Answer:**  
Quadratic loss with positive semi-definite Hessian.

---

## Q31. What is geometric interpretation of OLS?

**Answer:**  
Projection of y onto column space of X.

---

## Q32. What is residual vector geometrically?

**Answer:**  
Orthogonal to column space of X.

---

## Q33. Why are residuals orthogonal to features?

**Answer:**  
Property of least squares projection.

---

## Q34. What does R² represent geometrically?

**Answer:**  
Fraction of variance explained by projection.

---

## Q35. Why does adding features never decrease R²?

**Answer:**  
Projection space only expands.

---

## Q36. Why does adjusted R² penalize complexity?

**Answer:**  
Adjusts for degrees of freedom.

---

## Q37. What is degrees of freedom in Linear Regression?

**Answer:**  
Number of independent parameters estimated.

---

## Q38. Why does overparameterization cause instability?

**Answer:**  
Too many equivalent solutions.

---

## Q39. Why does Linear Regression extrapolate poorly?

**Answer:**  
Assumes linear trend beyond data.

---

## Q40. Key mathematical weakness of Linear Regression?

**Answer:**  
Strong assumptions on data structure.

---

📌 **Next:** Geometric interpretation — visualizing Linear Regression in vector spaces.

