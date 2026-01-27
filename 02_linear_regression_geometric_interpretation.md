# Linear Regression — Geometric Interpretation

This section builds **visual and geometric intuition** for Linear Regression. Once this clicks, PCA, SVD, and even Neural Networks feel natural.

---

## Q1. What space does Linear Regression operate in?

**Answer:**  
Linear Regression operates in **vector spaces**.

- Feature vectors lie in ℝᵖ  
- Target vector y lies in ℝⁿ

---

## Q2. What is the column space of X?

**Answer:**  
The subspace spanned by the columns of X.

**Intuition:**  
All predictions ŷ must lie in this space.

---

## Q3. What does OLS try to do geometrically?

**Answer:**  
Project y onto the column space of X.

---

## Q4. Why is projection the best approximation?

**Answer:**  
Projection minimizes Euclidean distance.

---

## Q5. What is the residual vector geometrically?

**Answer:**  
The difference between y and its projection.

---

## Q6. Why are residuals orthogonal to X?

**Answer:**  
Property of orthogonal projection.

---

## Q7. What does orthogonality mean here?

**Answer:**  
Residual has zero dot product with every column of X.

---

## Q8. Why is orthogonality important?

**Answer:**  
No linear combination of features can further reduce error.

---

## Q9. What happens geometrically when you add a feature?

**Answer:**  
Column space expands or stays same.

---

## Q10. Why does R² never decrease when adding features?

**Answer:**  
Projection space only grows.

---

## Q11. What is multicollinearity geometrically?

**Answer:**  
Columns of X are nearly linearly dependent.

---

## Q12. What does perfect multicollinearity look like?

**Answer:**  
One feature lies exactly in span of others.

---

## Q13. Why does multicollinearity cause unstable coefficients?

**Answer:**  
Many equivalent projections exist.

---

## Q14. What does scaling a feature do geometrically?

**Answer:**  
Stretches or compresses axis.

---

## Q15. Why doesn’t scaling change OLS solution?

**Answer:**  
Projection result remains invariant.

---

## Q16. Why does scaling change Gradient Descent path?

**Answer:**  
Contours become elongated ellipses.

---

## Q17. What does intercept term do geometrically?

**Answer:**  
Shifts the subspace away from origin.

---

## Q18. What happens if intercept is removed?

**Answer:**  
Projection forced through origin.

---

## Q19. How does noise appear geometrically?

**Answer:**  
Component of y orthogonal to column space.

---

## Q20. Why can’t Linear Regression fit arbitrary data?

**Answer:**  
Column space is limited.

---

## Q21. What is rank of X?

**Answer:**  
Dimension of column space.

---

## Q22. Why does low rank cause problems?

**Answer:**  
Loss of independent directions.

---

## Q23. What does pseudoinverse do geometrically?

**Answer:**  
Projects onto valid subspace only.

---

## Q24. How does Ridge Regression change geometry?

**Answer:**  
Shrinks projection toward origin.

---

## Q25. Why does Ridge fix multicollinearity?

**Answer:**  
Adds curvature to flat directions.

---

## Q26. How does Lasso differ geometrically?

**Answer:**  
Creates corners → sparsity.

---

## Q27. What does overfitting look like geometrically?

**Answer:**  
Projection follows noise directions.

---

## Q28. What does underfitting look like geometrically?

**Answer:**  
Projection misses major components of y.

---

## Q29. Why does LR extrapolate linearly?

**Answer:**  
Subspace extends infinitely.

---

## Q30. Biggest geometric limitation of Linear Regression?

**Answer:**  
Cannot bend to follow curved manifolds.

---

📌 **Next:** Tricky interview questions on Linear Regression (sign flips, p-values, scaling myths).