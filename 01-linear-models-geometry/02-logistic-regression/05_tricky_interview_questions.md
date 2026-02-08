# Logistic Regression — Tricky Interview Questions (Deep Explanations + Why)

This chapter focuses on **questions interviewers use to test depth**, not definitions. Each answer explains **what is happening, why it happens, and how to reason it out**.

---

## Q1. Why does Logistic Regression break under perfect class separation?

**What happens:**  
When a hyperplane can perfectly separate the two classes, the model keeps increasing the magnitude of weights.

**Why:**  
Increasing ||w|| pushes probabilities closer to 0 and 1, which increases likelihood indefinitely.

**Math intuition:**  
For correctly classified points, log loss → 0 as z → ±∞.

**Consequence:**  
No finite optimum exists.

**Fix:**  
Add regularization.

---

## Q2. Why do Logistic Regression coefficients sometimes become extremely large?

**Why:**  
- Near-perfect separation
- Highly correlated features
- Weak or no regularization

**Geometric view:**  
The model rotates and stretches the hyperplane to increase confidence.

---

## Q3. Why is accuracy a bad metric for Logistic Regression?

**What:**  
Accuracy ignores probability quality.

**Why:**  
Two models with same accuracy may have very different confidence calibration.

**Better thinking:**  
Logistic Regression is a **probability model**, not just a classifier.

---

## Q4. Why can two Logistic Regression models have identical accuracy but different ROC-AUC?

**Why:**  
Accuracy depends on a threshold; ROC-AUC measures ranking quality.

**Interpretation:**  
AUC checks whether positive samples are ranked above negatives.

**Visual:**  
ROC intuition:
https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc

---

## Q5. Why does threshold selection matter more than the model itself?

**Why:**  
Logistic Regression outputs probabilities, not decisions.

**Key idea:**  
The same model can behave very differently at thresholds 0.3 vs 0.7.

**Senior insight:**  
Model training and decision policy are separate problems.

---

## Q6. Why does Logistic Regression perform poorly on highly imbalanced data?

**Why:**  
Maximum likelihood favors the majority class.

**Effect:**  
Minority probabilities are systematically underestimated.

**Fixes:**  
- Class weights
- Resampling
- Proper metrics (PR-AUC)

---

## Q7. Why does ROC-AUC sometimes look good but precision is terrible?

**Why:**  
ROC ignores class prevalence.

**Interpretation:**  
High ranking quality does not guarantee useful positive predictions.

**Visual:**  
Precision–Recall intuition:
https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall

---

## Q8. Why is PR-AUC preferred for rare-event problems?

**Why:**  
It focuses on minority class performance.

**Real-world examples:**  
Fraud, disease detection, churn.

---

## Q9. Why does Logistic Regression sometimes outperform complex models?

**Why:**  
- Better bias–variance tradeoff
- Less overfitting
- Cleaner probability estimates

**Reality:**  
Simple models generalize better on noisy data.

---

## Q10. Can Logistic Regression overfit?

**Yes — why:**  
- Many features
- Small dataset
- Weak regularization

**Misconception:**  
Overfitting is not limited to non-linear models.

---

## Q11. Why do Logistic Regression coefficients flip sign after adding features?

**Why:**  
Coefficients represent **conditional effects**.

**Interpretation:**  
The model redistributes explanatory power among correlated features.

---

## Q12. Does coefficient sign flip mean the model is wrong?

**No — why:**  
Prediction may remain stable while interpretation changes.

**Lesson:**  
Interpret coefficients only when features are weakly correlated.

---

## Q13. Why is Logistic Regression sensitive to feature scaling?

**Why:**  
Optimization depends on gradient geometry.

**Effect:**  
Unscaled features create elongated loss contours → slow convergence.

---

## Q14. Why does L1 regularization lead to sparse Logistic Regression?

**Why:**  
L1 penalty creates corners in optimization space.

**Geometry:**  
Optimum hits axes → zero coefficients.

---

## Q15. Why does Logistic Regression give calibrated probabilities?

**Why:**  
Log loss is a proper scoring rule.

**Interpretation:**  
The model is penalized for misrepresenting uncertainty.

---

## Q16. When should you distrust Logistic Regression probabilities?

**Cases:**  
- Severe dataset shift
- Feedback loops
- Training labels are biased

---

## Q17. Why does adding interaction terms change interpretation drastically?

**Why:**  
Main effects become conditional on other features.

**Senior warning:**  
Coefficient interpretation becomes non-intuitive.

---

## Q18. Is Logistic Regression a generative model?

**Answer:**  
No.

**Why:**  
It models P(y|x), not P(x|y).

---

## Q19. Why is Logistic Regression preferred in regulated industries?

**Why:**  
- Transparency
- Stability
- Explainability

---

## Q20. Biggest interview misconception about Logistic Regression?

**Answer:**  
Thinking it predicts classes instead of probabilities.

---

📌 **Next:** Real-world Logistic Regression project issues — imbalance, calibration drift, threshold tuning, and deployment reality.

