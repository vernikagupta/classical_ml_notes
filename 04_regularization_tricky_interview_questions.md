# Regularization — Tricky Interview Questions (Depth Checks + Real Reasoning)

This chapter covers **questions interviewers use to test whether you actually understand regularization** or are just repeating buzzwords. Each answer explains **what**, **why**, and **how to reason it out**.

---

## Q1. Does regularization always improve test performance?

**Short answer:**  
No.

**Why:**  
Regularization increases bias while reducing variance.

**Reasoning:**  
If the model is already underfitting, adding regularization worsens performance.

**Interview trap:**  
Saying “regularization always helps generalization”.

---

## Q2. Why does Lasso sometimes perform worse than Ridge?

**Why:**  
- Lasso introduces higher bias
- It may drop useful but correlated features

**Geometry reminder:**  
The diamond corner forces hard choices.

---

## Q3. Why does Lasso behave unstably with correlated features?

**Why:**  
Multiple features explain the same variance.

**Effect:**  
Lasso arbitrarily picks one and drops the rest.

**Real consequence:**  
Different train splits → different selected features.

---

## Q4. Why is ElasticNet preferred in many real projects?

**Why:**  
- L1 gives sparsity
- L2 gives stability

**Senior answer:**  
ElasticNet is robust when features are correlated.

---

## Q5. Why must features be scaled before regularization?

**Why:**  
Penalties depend on coefficient magnitude.

**Without scaling:**  
Features with larger units are penalized more.

**Trap:**  
Forgetting scaling biases feature selection.

---

## Q6. Why does Ridge not perform feature selection?

**Why:**  
L2 penalty is smooth.

**Result:**  
Coefficients shrink continuously but rarely reach zero.

---

## Q7. Can Ridge coefficients ever be exactly zero?

**Answer:**  
Only in degenerate cases.

**Reason:**  
No corners in constraint region.

---

## Q8. Why does L1 regularization break differentiability?

**Why:**  
Absolute value has a kink at zero.

**Consequence:**  
No closed-form solution.

---

## Q9. How does regularization help with multicollinearity?

**Why:**  
It stabilizes coefficient estimates.

**Math intuition:**  
Small eigenvalues are inflated.

---

## Q10. Why does regularization not remove data leakage?

**Why:**  
Leakage is a data problem, not a model complexity problem.

**Interview insight:**  
Regularization cannot fix bad validation strategy.

---

## Q11. Why does increasing λ too much hurt performance?

**Why:**  
The model becomes overly constrained.

**Result:**  
High bias, underfitting.

---

## Q12. Can regularization replace cross-validation?

**Answer:**  
No.

**Why:**  
λ itself must be tuned using validation.

---

## Q13. Why is regularization considered a form of prior?

**Why:**  
It encodes belief that weights should be small.

**Bayesian view:**  
Ridge → Gaussian prior, Lasso → Laplace prior.

---

## Q14. Why does Lasso sometimes select too few features?

**Why:**  
Strong sparsity pressure.

**Effect:**  
Important but weak features are dropped.

---

## Q15. Why does regularization affect interpretability?

**Why:**  
Coefficient magnitude is influenced by penalty.

**Implication:**  
Interpret coefficients carefully.

---

## Q16. Is early stopping a form of regularization?

**Answer:**  
Yes.

**Why:**  
It limits effective model complexity.

---

## Q17. Why does dropout act like regularization?

**Why:**  
It injects noise during training.

**Effect:**  
Reduces reliance on specific weights.

---

## Q18. When should you NOT use Lasso?

**Cases:**  
- Highly correlated features
- Need stable coefficients

---

## Q19. When should you NOT use Ridge?

**Cases:**  
- Need feature selection
- Many irrelevant features

---

## Q20. Biggest regularization misconception?

**Answer:**  
That it magically fixes poor data.

---

📌 **Next:** Real-world regularization mistakes and best practices in production systems.