# Missing Data Imputation – 100 Interview & Scenario-Based Questions (Industry Level)

These questions are **not textbook questions**. They are framed the way **real interviewers and real projects** think about missing data.

Each answer explains:
- **What the right choice is**
- **Why it works**
- **Why alternatives fail**

---

## Section A: Foundations & Thinking (Q1–Q20)

### Q1. Why is missing data handling a modeling decision and not just preprocessing?
**Answer:**
Because missingness often contains **information about the data-generating process**. If missingness is correlated with the target (MNAR), imputation changes the conditional distribution \( P(y|X) \). Treating it as preprocessing ignores bias introduction, variance shrinkage, and signal loss.

---

### Q2. What is the first question you ask when you see missing values?
**Answer:**
"Why is this data missing?" not "How much is missing?". The *reason* determines whether missingness is MCAR, MAR, or MNAR, which directly dictates the valid imputation strategy.

---

### Q3. Why is MCAR the safest assumption but also the rarest in practice?
**Answer:**
MCAR assumes missingness is independent of both features and target. Real systems rarely behave randomly; missingness usually comes from user behavior, system failures, or business rules, making MCAR uncommon.

---

### Q4. What statistical bias is introduced by mean imputation?
**Answer:**
Mean imputation reduces variance and attenuates correlations. This biases coefficient estimates toward zero in linear models and underestimates uncertainty.

---

### Q5. Why does median imputation often outperform mean in practice?
**Answer:**
Because real-world features are skewed and contain outliers. Median is robust and does not assume symmetry, reducing distortion.

---

### Q6. When is dropping rows with missing values acceptable?
**Answer:**
Only when missingness is MCAR **and** the dropped proportion is small. Otherwise, it introduces sample selection bias.

---

### Q7. Why is MNAR the most dangerous type of missingness?
**Answer:**
Because the probability of missingness depends on the unobserved value itself, making naive imputation systematically biased.

---

### Q8. How do missing indicators help models?
**Answer:**
They explicitly model missingness as a feature, allowing the model to learn missingness patterns instead of hiding them inside imputed values.

---

### Q9. Why can missing indicators hurt performance sometimes?
**Answer:**
In small datasets, indicators can overfit noise. They add dimensions that may not generalize.

---

### Q10. Why should imputation be done after train-test split?
**Answer:**
To avoid data leakage. Computing statistics on full data lets test information influence training.

---

### Q11. Why is missingness monitoring critical in production?
**Answer:**
Because missingness drift is a form of data drift and often the earliest signal of upstream system failures.

---

### Q12. Can missing data ever improve model performance?
**Answer:**
Yes—when missingness itself encodes signal (MNAR), adding indicators can improve performance.

---

### Q13. Why is mean imputation especially harmful for KNN models?
**Answer:**
KNN relies on distance. Mean imputation collapses distances and distorts neighborhood structure.

---

### Q14. Why does imputation affect interpretability?
**Answer:**
Because coefficients may reflect imputation artifacts rather than true relationships.

---

### Q15. What is variance shrinkage in imputation?
**Answer:**
Replacing missing values with constants reduces feature variance, leading to overconfident models.

---

### Q16. Why is domain knowledge critical in missing data handling?
**Answer:**
Because statistical assumptions alone cannot explain business-driven missingness.

---

### Q17. Why should different features use different imputation strategies?
**Answer:**
Because missingness mechanisms differ by feature; one-size-fits-all introduces bias.

---

### Q18. How does missing data interact with regularization?
**Answer:**
Regularization may suppress indicator features, hiding missingness signals.

---

### Q19. Why do interviewers ask about MNAR so often?
**Answer:**
Because handling MNAR correctly separates senior practitioners from juniors.

---

### Q20. What is the biggest misconception about missing data?
**Answer:**
That filling values restores the original data distribution. It never does.

---

## Section B: Method Selection Scenarios (Q21–Q40)

### Q21. Income is missing mostly for high-income users. What do you do?
**Answer:**
Treat as MNAR. Use median imputation + missing indicator. Never use mean alone.

---

### Q22. Sensor data has short random gaps. Best method?
**Answer:**
Interpolation or forward fill, assuming no regime change.

---

### Q23. Salary is confidential and often missing. Strategy?
**Answer:**
Domain constant (e.g., -1) + missing indicator.

---

### Q24. Age is missing randomly for 1% rows. Strategy?
**Answer:**
Median imputation without indicator is acceptable.

---

### Q25. Categorical feature has missing due to “not applicable”.
**Answer:**
Create explicit category: `Not_Applicable`.

---

### Q26. Why is mode imputation risky for categorical features?
**Answer:**
It inflates the majority class and biases class probabilities.

---

### Q27. When is KNN imputation justified?
**Answer:**
When features are strongly correlated and properly scaled.

---

### Q28. Why does KNN imputation fail in high dimensions?
**Answer:**
Distance concentration makes neighbors meaningless.

---

### Q29. When should you use MICE?
**Answer:**
When MAR assumption holds and dataset size allows.

---

### Q30. Why is MICE rarely used in production?
**Answer:**
It is slow, unstable, and hard to monitor.

---

### Q31. Can neural networks handle missing values natively?
**Answer:**
No. They require explicit imputation or masking.

---

### Q32. Why are tree-based models special with missing data?
**Answer:**
They learn split directions for missing values.

---

### Q33. Why can tree missing paths overfit?
**Answer:**
Because missingness creates artificial splits.

---

### Q34. Should you still add indicators for trees?
**Answer:**
Yes, especially for MNAR.

---

### Q35. Why is standardization required before KNN imputation?
**Answer:**
To prevent scale dominance in distance computation.

---

### Q36. What happens if you impute time-series using backfill?
**Answer:**
You leak future information.

---

### Q37. Why is interpolation dangerous across regime changes?
**Answer:**
It smooths real structural breaks.

---

### Q38. What should you do with long sensor outages?
**Answer:**
Model them explicitly; do not interpolate blindly.

---

### Q39. Why should imputed segments be flagged?
**Answer:**
So models can learn reliability of values.

---

### Q40. Why do linear models suffer more from bad imputation than trees?
**Answer:**
They assume linearity and are sensitive to distribution shifts.

---

## Section C: Production & MLOps (Q41–Q70)

### Q41. What is missingness drift?
**Answer:**
Change in missing rate or pattern over time.

---

### Q42. Why is missingness drift often an early warning signal?
**Answer:**
It indicates upstream pipeline or behavior changes.

---

### Q43. Should imputers be retrained?
**Answer:**
Yes, along with the model.

---

### Q44. Why is freezing imputers risky?
**Answer:**
Because data distributions evolve.

---

### Q45. How do you monitor missingness in production?
**Answer:**
Track missing % per feature and indicator drift.

---

### Q46. What alert thresholds are reasonable?
**Answer:**
Domain-specific; typically relative change >20–30%.

---

### Q47. Why is imputing before pipelines dangerous?
**Answer:**
It breaks reproducibility and auditability.

---

### Q48. How do imputers affect explainability tools?
**Answer:**
SHAP values may attribute importance to imputation artifacts.

---

### Q49. Why must imputers be versioned?
**Answer:**
For reproducibility and rollback.

---

### Q50. How do missing indicators help monitoring?
**Answer:**
They act as sensors for data health.

---

### Q51. What happens if missingness correlates with deployment environment?
**Answer:**
Model performance degrades silently.

---

### Q52. Should test data ever influence imputation?
**Answer:**
Never.

---

### Q53. Why is backfilling historical data risky?
**Answer:**
It rewrites history and breaks temporal integrity.

---

### Q54. How does missing data affect fairness?
**Answer:**
If missingness correlates with protected groups, bias increases.

---

### Q55. Why do audits care about missing data logic?
**Answer:**
Because it affects decision outcomes.

---

### Q56. How do you explain missing data choices to stakeholders?
**Answer:**
By linking them to business behavior.

---

### Q57. What is the worst production mistake with missing data?
**Answer:**
Silently imputing and never monitoring.

---

### Q58. Why is missing data a reliability issue, not just ML?
**Answer:**
It reflects system health.

---

### Q59. Can missingness invalidate offline validation?
**Answer:**
Yes, if patterns differ online.

---

### Q60. Why do models fail suddenly after months in production?
**Answer:**
Missingness drift is a common cause.

---

### Q61. Should you impute streaming data differently?
**Answer:**
Yes—respect causality and latency constraints.

---

### Q62. How does missingness interact with concept drift?
**Answer:**
They often occur together.

---

### Q63. Why is missingness often seasonal?
**Answer:**
User behavior and system load vary seasonally.

---

### Q64. Should missingness be part of data contracts?
**Answer:**
Yes.

---

### Q65. Why do tree models hide missingness problems initially?
**Answer:**
They overfit missing paths.

---

### Q66. How do you debug sudden missing spikes?
**Answer:**
Check ingestion, schema changes, upstream services.

---

### Q67. What is a safe retraining trigger?
**Answer:**
Combined missingness + performance degradation.

---

### Q68. Why should indicators be logged separately?
**Answer:**
For interpretability and alerts.

---

### Q69. Why is missing data handling part of governance?
**Answer:**
It directly affects decisions.

---

### Q70. What distinguishes senior handling of missing data?
**Answer:**
They reason about causes, not just fixes.

---

## Section D: Tricky & Advanced (Q71–Q100)

### Q71. Can imputation ever create spurious correlations?
**Answer:**
Yes, especially mean imputation.

---

### Q72. Why does interpolation reduce variance artificially?
**Answer:**
It smooths noise.

---

### Q73. How do you test MNAR assumptions?
**Answer:**
Sensitivity analysis, indicators, domain validation.

---

### Q74. Why is MNAR fundamentally untestable statistically?
**Answer:**
Because it depends on unobserved values.

---

### Q75. Can missing data affect ranking models differently?
**Answer:**
Yes, rank stability is sensitive to imputation.

---

### Q76. Why does mean imputation bias coefficients toward zero?
**Answer:**
It shrinks variance.

---

### Q77. How do you explain missingness bias to non-technical stakeholders?
**Answer:**
Using behavior-driven examples.

---

### Q78. Should missingness be included in feature selection?
**Answer:**
Yes, indicators can be important.

---

### Q79. Why is imputation harder in multi-source data?
**Answer:**
Different missing mechanisms coexist.

---

### Q80. How does missing data affect causal inference?
**Answer:**
It biases treatment effect estimates.

---

### Q81. Why is imputing labels dangerous?
**Answer:**
It fabricates ground truth.

---

### Q82. How do embeddings handle missing values?
**Answer:**
Typically via masking or special tokens.

---

### Q83. Why is missingness critical in recommender systems?
**Answer:**
Absence of interaction is ambiguous.

---

### Q84. Why is zero not always a neutral imputation?
**Answer:**
It introduces artificial meaning.

---

### Q85. How do you audit missing data logic?
**Answer:**
Trace feature lineage and decisions.

---

### Q86. Can imputation violate regulatory rules?
**Answer:**
Yes, if undocumented.

---

### Q87. Why do ensemble models react differently to imputation?
**Answer:**
They aggregate biases.

---

### Q88. What is partial pooling in missing data?
**Answer:**
Group-based shrinkage.

---

### Q89. Why are indicators sometimes more important than imputed values?
**Answer:**
They encode behavior.

---

### Q90. How does missing data interact with feature scaling?
**Answer:**
Scaling before imputation leaks information.

---

### Q91. Why should missingness be visualized?
**Answer:**
Patterns reveal causes.

---

### Q92. What is the most interview-winning insight on missing data?
**Answer:**
Missingness itself is data.

---

### Q93. How do you handle missing data in online learning?
**Answer:**
Use causal, streaming-safe strategies.

---

### Q94. Why does imputation complicate A/B testing?
**Answer:**
It alters distributions differently across groups.

---

### Q95. Why is imputation dangerous in anomaly detection?
**Answer:**
It hides anomalies.

---

### Q96. Why do GAN-based imputations fail in production?
**Answer:**
They hallucinate data.

---

### Q97. When should you not impute at all?
**Answer:**
When missingness defines the event.

---

### Q98. How does missingness affect confidence calibration?
**Answer:**
It increases overconfidence.

---

### Q99. Why do experienced teams document imputation logic?
**Answer:**
For auditability and trust.

---

### Q100. One-line senior takeaway?
**Answer:**
> *If you don’t model missingness, missingness will model your results.*
