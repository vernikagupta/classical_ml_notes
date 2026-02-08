# Foundations of Machine Learning — Real-World Scenarios

This section captures **what actually breaks ML systems in production**. Interviewers use these scenarios to assess whether you have *worked with ML beyond notebooks*.

---

## Q1. Model performs well offline but poorly in production. Why?

**Answer:**  
- Data leakage during training
- Train–serve skew
- Distribution shift
- Wrong evaluation metric

**Senior thinking:**  
Check data first, not the model.

---

## Q2. What is train–serve skew?

**Answer:**  
Mismatch between features at training time and inference time.

**Example:**  
Aggregations computed differently online.

---

## Q3. What is data drift?

**Answer:**  
Input distribution P(X) changes over time.

**Example:**  
User behavior changes seasonally.

---

## Q4. What is concept drift?

**Answer:**  
Relationship between X and y changes.

**Example:**  
Fraud patterns evolve.

---

## Q5. How do you detect data drift?

**Answer:**  
- Statistical tests
- Feature distribution monitoring
- Population stability index

---

## Q6. Why do ML models silently degrade?

**Answer:**  
Because predictions are not directly labeled in real time.

---

## Q7. Why is retraining blindly dangerous?

**Answer:**  
It may reinforce bias or noise.

---

## Q8. What is target leakage in real projects?

**Answer:**  
Using future information unknowingly.

**Example:**  
Using post-event timestamps.

---

## Q9. Why do feature pipelines matter more than models?

**Answer:**  
Features encode domain knowledge.

---

## Q10. Why does feature importance change over time?

**Answer:**  
Underlying behavior shifts.

---

## Q11. How do you debug a failing model?

**Answer:**  
- Check input distributions
- Compare train vs inference features
- Slice metrics

---

## Q12. What is slicing metrics?

**Answer:**  
Evaluating performance across subgroups.

---

## Q13. Why does accuracy drop but business KPI stays stable?

**Answer:**  
Metric does not align with business objective.

---

## Q14. Why do ML teams prefer simple models in production?

**Answer:**  
Interpretability, stability, latency.

---

## Q15. What is cold-start problem?

**Answer:**  
Lack of historical data for new users or items.

---

## Q16. Why does ML fail on small data?

**Answer:**  
Variance dominates signal.

---

## Q17. How do you choose features in real projects?

**Answer:**  
Start with domain logic, not correlation.

---

## Q18. Why does adding features hurt production performance?

**Answer:**  
Latency, leakage, instability.

---

## Q19. What is shadow deployment?

**Answer:**  
Running a model without affecting decisions.

---

## Q20. Why are A/B tests needed for ML?

**Answer:**  
Offline metrics do not capture real impact.

---

## Q21. What is feedback loop in ML systems?

**Answer:**  
Model predictions influence future data.

---

## Q22. Why does personalization amplify bias?

**Answer:**  
Model sees biased feedback.

---

## Q23. What is model staleness?

**Answer:**  
Model no longer reflects current data.

---

## Q24. Why do thresholds matter in production?

**Answer:**  
They control trade-offs between business costs.

---

## Q25. Biggest real-world ML mistake?

**Answer:**  
Treating ML as a one-time training task.

---

📌 **Foundations complete. Next: Linear Regression — from geometry to derivation to failure modes.**