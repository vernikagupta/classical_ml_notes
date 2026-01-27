# Linear Regression — Tricky Interview Questions

This section targets **classic and advanced traps** interviewers use to test *depth over memorization*. Each question reflects confusion seen in real interviews.

---

## Q1. Can Linear Regression overfit?

**Answer:**  
Yes.

**Why this is tricky:**  
Many think only complex models overfit.

**Correct intuition:**  
With many features or small data, LR has high variance.

---

## Q2. Why do regression coefficients flip sign after adding a new feature?

**Answer:**  
Because the model redistributes explained variance among correlated features.

**Key idea:**  
Coefficients are *conditional effects*, not marginal effects.

---

## Q3. Does coefficient sign flip mean the model is wrong?

**Answer:**  
No.

**Reality:**  
Prediction may remain stable while interpretation changes.

---

## Q4. Why do p-values change when you add or remove features?

**Answer:**  
Standard errors depend on correlation structure.

---

## Q5. Can a coefficient be statistically insignificant but still useful?

**Answer:**  
Yes.

**Reason:**  
Prediction ≠ inference.

---

## Q6. Why does Linear Regression sometimes outperform XGBoost?

**Answer:**  
When data is small, noisy, or mostly linear.

---

## Q7. Why does scaling affect Gradient Descent but not OLS?

**Answer:**  
OLS solution is invariant to scaling; GD path is not.

---

## Q8. Why does adding features always increase R² but not performance?

**Answer:**  
OLS fits noise; generalization may worsen.

---

## Q9. Can R² be used for model comparison across datasets?

**Answer:**  
No.

---

## Q10. Why is high R² sometimes suspicious?

**Answer:**  
Possible leakage or overfitting.

---

## Q11. Does multicollinearity reduce model accuracy?

**Answer:**  
Not necessarily.

---

## Q12. Why does multicollinearity inflate variance but not bias?

**Answer:**  
Expected coefficient value is unchanged; uncertainty increases.

---

## Q13. Can you trust feature importance from Linear Regression?

**Answer:**  
Only if features are weakly correlated.

---

## Q14. Why does Linear Regression fail badly on time series data?

**Answer:**  
Violates independence and stationarity assumptions.

---

## Q15. Is Linear Regression sensitive to outliers?

**Answer:**  
Yes.

**Why:**  
Squared loss magnifies large errors.

---

## Q16. Why is MAE more robust to outliers than MSE?

**Answer:**  
Linear penalty instead of quadratic.

---

## Q17. Should you always remove outliers in regression?

**Answer:**  
No.

**Senior view:**  
First understand why they exist.

---

## Q18. Why does adding polynomial features increase overfitting risk?

**Answer:**  
Expands hypothesis space.

---

## Q19. Can Linear Regression handle non-linear relationships?

**Answer:**  
Yes, through feature engineering.

---

## Q20. What is Simpson’s Paradox in regression?

**Answer:**  
Trend reverses when conditioning on a variable.

---

## Q21. Why is Simpson’s Paradox dangerous?

**Answer:**  
Leads to wrong causal conclusions.

---

## Q22. Does adding interaction terms always help?

**Answer:**  
No.

---

## Q23. Why do regression models extrapolate poorly?

**Answer:**  
They assume same linear trend outside data range.

---

## Q24. Is Linear Regression a generative model?

**Answer:**  
No.

---

## Q25. Biggest misconception about Linear Regression?

**Answer:**  
That it is too simple to be useful.

---

📌 **Next:** Real-world Linear Regression project issues — leakage, outliers, business interpretation.