# Foundations of Machine Learning — Tricky Interview Questions

This section contains **questions that expose shallow understanding**. Interviewers use these to separate people who *use ML* from people who *understand ML*.

---

## Q1. If training error is low and test error is high, what is happening?

**Answer:**  
The model is overfitting.

**Why this is tricky:**  
Many candidates say “need more data” without checking model complexity.

**Correct thinking:**  
Reduce variance: simplify model, regularize, or add data.

---

## Q2. If both training and test error are high, what is happening?

**Answer:**  
Underfitting.

**Trap:**  
Adding regularization will make it worse.

---

## Q3. Can a model have low bias and low variance?

**Answer:**  
Only if the data is simple and abundant.

**Why:**  
Bias–variance tradeoff is data dependent.

---

## Q4. Does high accuracy mean a good model?

**Answer:**  
Not necessarily.

**Example:**  
99% accuracy on a 1% fraud dataset is useless.

---

## Q5. Can increasing data ever increase overfitting?

**Answer:**  
No, if data is i.i.d.

**Trap:**  
If data is correlated or leaked, then yes.

---

## Q6. Why does test error sometimes increase after adding features?

**Answer:**  
Added features introduce noise and increase variance.

---

## Q7. Is more complex model always better with more data?

**Answer:**  
Only if added complexity matches true structure.

---

## Q8. Why does scaling affect KNN but not Decision Trees?

**Answer:**  
KNN relies on distance; trees rely on thresholds.

---

## Q9. Can you use accuracy as loss function?

**Answer:**  
No.

**Why:**  
Accuracy is non-differentiable.

---

## Q10. Why don’t we directly optimize F1-score?

**Answer:**  
It’s non-smooth and non-convex.

---

## Q11. Does lower loss always mean better metric?

**Answer:**  
No.

**Example:**  
Log loss improves but recall worsens.

---

## Q12. If a model overfits, should you always add regularization?

**Answer:**  
No.

**Correct thinking:**  
Check data leakage, feature leakage, and validation strategy first.

---

## Q13. Why can cross-validation give optimistic results?

**Answer:**  
If data is not i.i.d. (time, user, group leakage).

---

## Q14. Is cross-validation always better than a single split?

**Answer:**  
No.

**Example:**  
Time-series forecasting.

---

## Q15. Why does random seed affect model results?

**Answer:**  
Initialization, sampling, and data splits are stochastic.

---

## Q16. Should you fix random seed in production?

**Answer:**  
Yes, for reproducibility — but monitor drift.

---

## Q17. Can a model generalize without regularization?

**Answer:**  
Yes, if hypothesis space is already constrained.

---

## Q18. Why does adding noise sometimes improve generalization?

**Answer:**  
It prevents the model from memorizing.

---

## Q19. Is test set used only once?

**Answer:**  
Ideally yes.

**Trap:**  
Repeated tuning leaks information.

---

## Q20. Why is validation set performance unstable?

**Answer:**  
Small sample size or high variance model.

---

## Q21. If validation loss oscillates, what does it indicate?

**Answer:**  
Learning rate too high or noisy gradients.

---

## Q22. Can a simple model beat a complex one?

**Answer:**  
Yes, when data is limited or noisy.

---

## Q23. Why is ML called function approximation?

**Answer:**  
Because we approximate unknown mappings.

---

## Q24. If model predictions look reasonable but metrics are bad, why?

**Answer:**  
Wrong metric, wrong threshold, or class imbalance.

---

## Q25. Why does shuffling labels break learning?

**Answer:**  
There is no signal to learn.

---

## Q26. What does learning curve diagnose?

**Answer:**  
Bias vs variance problems.

---

## Q27. Can you compare models trained on different splits?

**Answer:**  
Not reliably.

---

## Q28. Why does adding features after splitting matter?

**Answer:**  
Feature engineering before split causes leakage.

---

## Q29. Why is ML evaluation harder than training?

**Answer:**  
Because real-world data changes.

---

## Q30. Biggest misconception about ML?

**Answer:**  
That algorithms matter more than data.

---

📌 **Next:** Real-world ML scenarios — how models fail after deployment and how seniors debug them.