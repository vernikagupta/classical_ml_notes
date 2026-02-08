# Linear Regression — Real-World Project Issues

This section covers **how Linear Regression behaves in real production projects**, where data is messy, assumptions break, and business interpretation matters more than theory.

---

## Q1. Why is Linear Regression still widely used in industry?

**Answer:**  
- Interpretability
- Stability
- Low latency
- Easier debugging

**Reality:**  
In many business problems, simplicity beats marginal accuracy gains.

---

## Q2. When does Linear Regression outperform complex models?

**Answer:**  
- Small or medium-sized datasets
- High noise
- Mostly linear relationships
- Strong domain-driven features

---

## Q3. What is feature leakage in regression projects?

**Answer:**  
Using information that would not be available at prediction time.

**Example:**  
Using post-outcome aggregates.

---

## Q4. Why is leakage especially dangerous in regression?

**Answer:**  
Because high R² hides the problem.

---

## Q5. Why do regression coefficients often mislead stakeholders?

**Answer:**  
Because correlation is mistaken for causation.

---

## Q6. Can we interpret coefficients causally?

**Answer:**  
Only under very strong assumptions.

---

## Q7. Why do coefficients change across retraining cycles?

**Answer:**  
Sampling variability and feature correlation.

---

## Q8. How do you explain coefficient instability to business teams?

**Answer:**  
Focus on prediction consistency, not exact values.

---

## Q9. How do outliers affect Linear Regression in practice?

**Answer:**  
They disproportionately influence coefficients.

---

## Q10. Should you always remove outliers?

**Answer:**  
No.

**Correct approach:**  
Investigate their origin first.

---

## Q11. What are practical ways to handle outliers?

**Answer:**  
- Log-transform target
- Winsorization
- Robust loss functions (Huber)

---

## Q12. When is Huber loss preferred?

**Answer:**  
When data has occasional extreme errors.

---

## Q13. Why does Linear Regression struggle with skewed targets?

**Answer:**  
Squared loss assumes symmetric errors.

---

## Q14. How do you fix skewed target distributions?

**Answer:**  
Apply log or Box-Cox transformations.

---

## Q15. Why does Linear Regression break on time series data?

**Answer:**  
Autocorrelation violates independence.

---

## Q16. Can Linear Regression still be used for time series?

**Answer:**  
Yes, with lag features and careful validation.

---

## Q17. Why is validation strategy critical in regression projects?

**Answer:**  
Wrong splits cause optimistic performance.

---

## Q18. Why do production metrics drift even if training metrics are stable?

**Answer:**  
Data drift and changing behavior.

---

## Q19. How do you monitor a regression model in production?

**Answer:**  
- Input distribution checks
- Residual tracking
- Segment-wise errors

---

## Q20. Why do stakeholders prefer Linear Regression explanations?

**Answer:**  
Coefficients map directly to business levers.

---

## Q21. Why are p-values rarely trusted in production?

**Answer:**  
Assumptions rarely hold in real data.

---

## Q22. Should you drop insignificant features?

**Answer:**  
Not always — prediction may still benefit.

---

## Q23. Why does Linear Regression work well in regulated industries?

**Answer:**  
Transparency and auditability.

---

## Q24. What is the biggest real-world mistake with Linear Regression?

**Answer:**  
Over-interpreting coefficients.

---

## Q25. When should you move beyond Linear Regression?

**Answer:**  
When strong non-linearity or interactions dominate.

---

📌 **Linear Regression complete. Next: Logistic Regression — classification with probability, geometry, and odds.**