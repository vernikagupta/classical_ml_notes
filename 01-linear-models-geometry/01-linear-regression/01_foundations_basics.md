# Foundations of Machine Learning — Basics

This section builds **rock-solid intuition** for Machine Learning before any algorithm. Most interview failures happen here.

---

## Q1. What is Machine Learning?

**Answer:**  
Machine Learning is the process of learning a function that maps inputs to outputs using data instead of explicit rules.

**Intuition:**  
We are approximating an unknown data-generating process.

**Interview trap:**  
Saying "ML is AI" or "ML is automation".

**In real projects:**  
ML is used when rules are too complex or change over time.

---

## Q2. What are the core components of an ML problem?

**Answer:**  
- Data
- Features
- Model
- Loss function
- Optimization method
- Evaluation metric

**Why this matters:**  
Most debugging involves one of these being wrong.

---

## Q3. What is the difference between supervised and unsupervised learning?

**Answer:**  
Supervised learning uses labeled data; unsupervised learning does not.

**Geometric intuition:**  
Supervised learning fits boundaries; unsupervised learning discovers structure.

---

## Q4. What is a hypothesis space?

**Answer:**  
The set of all functions a model can represent.

**Math intuition:**  
Linear regression hypothesis:  
ŷ = wᵀx + b

**Interview trap:**  
Bigger hypothesis space ≠ better model.

---

## Q5. What is inductive bias?

**Answer:**  
Assumptions a model makes to generalize beyond seen data.

**Examples:**  
- Linear models assume linearity
- KNN assumes locality

---

## Q6. What is generalization?

**Answer:**  
Model performance on unseen data.

**Key idea:**  
Good training performance ≠ good generalization.

---

## Q7. What is overfitting?

**Answer:**  
Model learns noise instead of signal.

**Geometry intuition:**  
Decision boundary becomes unnecessarily complex.

---

## Q8. What is underfitting?

**Answer:**  
Model is too simple to capture structure.

---

## Q9. Explain bias–variance tradeoff.

**Answer:**  
Bias is error from wrong assumptions; variance is error from sensitivity to data.

**Key equation:**  
Total Error = Bias² + Variance + Noise

---

## Q10. Why does more data reduce variance but not bias?

**Answer:**  
More data stabilizes estimates but does not change model assumptions.

---

## Q11. What is empirical risk minimization?

**Answer:**  
Minimizing average loss on training data.

**Math:**  
Risk = (1/n) Σ L(yᵢ, ŷᵢ)

---

## Q12. What is the difference between parametric and non-parametric models?

**Answer:**  
Parametric models have fixed parameters; non-parametric grow with data.

---

## Q13. Why do we split data into train, validation, and test?

**Answer:**  
To prevent data leakage and over-optimistic estimates.

---

## Q14. What is data leakage?

**Answer:**  
Using information unavailable at prediction time.

**Real-world example:**  
Target encoding before splitting.

---

## Q15. Why is shuffling data important?

**Answer:**  
Prevents temporal or grouped bias.

---

## Q16. What is feature scaling?

**Answer:**  
Bringing features to comparable ranges.

**Why:**  
Distance- and gradient-based models depend on scale.

---

## Q17. Difference between normalization and standardization?

**Answer:**  
Normalization rescales to [0,1]; standardization centers to mean 0, variance 1.

---

## Q18. Why does scaling not matter for tree models?

**Answer:**  
Trees use threshold splits, not distances.

---

## Q19. What is loss function vs metric?

**Answer:**  
Loss is optimized; metric is reported.

---

## Q20. Why do we use convex loss functions?

**Answer:**  
They guarantee global minima.

---

## Q21. What is gradient descent intuitively?

**Answer:**  
Iteratively moving downhill on loss surface.

---

## Q22. What is learning rate?

**Answer:**  
Step size in optimization.

**Trap:**  
Too high → divergence; too low → slow convergence.

---

## Q23. What is a local minimum?

**Answer:**  
Point where gradient is zero but not global minimum.

---

## Q24. What is convex vs non-convex optimization?

**Answer:**  
Convex problems have one minimum; non-convex have many.

---

## Q25. Why is ML probabilistic?

**Answer:**  
Because data is noisy and incomplete.

---

## Q26. What assumptions does ML always make?

**Answer:**  
- Train and test data come from same distribution
- Patterns repeat

---

## Q27. What is i.i.d assumption?

**Answer:**  
Independent and identically distributed samples.

---

## Q28. When does i.i.d fail?

**Answer:**  
Time series, recommendation systems, fraud detection.

---

## Q29. What is concept drift?

**Answer:**  
Relationship between X and y changes over time.

---

## Q30. What makes ML fail in production?

**Answer:**  
- Data drift
- Bad features
- Wrong metric
- Leakage

---

## Q31. Why accuracy is a bad metric sometimes?

**Answer:**  
Class imbalance hides poor performance.

---

## Q32. What is precision vs recall intuitively?

**Answer:**  
Precision = correctness of positives
Recall = coverage of positives

---

## Q33. What is ROC curve?

**Answer:**  
Tradeoff between TPR and FPR.

---

## Q34. Why AUC is threshold independent?

**Answer:**  
It measures ranking quality.

---

## Q35. What is cross-validation?

**Answer:**  
Repeated train-test splits to estimate generalization.

---

## Q36. When should you NOT use cross-validation?

**Answer:**  
Time series or grouped data.

---

## Q37. What is bootstrapping?

**Answer:**  
Sampling with replacement.

---

## Q38. What is ensemble learning?

**Answer:**  
Combining multiple models.

---

## Q39. Why ensembles work?

**Answer:**  
They reduce variance and bias.

---

## Q40. What is the most important ML skill?

**Answer:**  
Problem formulation, not algorithms.

---

📌 **Next:** Mathematical intuition of bias–variance, risk minimization, and geometry of learning.