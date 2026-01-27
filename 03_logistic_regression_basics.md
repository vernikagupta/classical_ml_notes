# Logistic Regression — Basics (Deep Intuition + Math + Geometry)

This file explains Logistic Regression **slowly, deeply, and completely**.
Every answer contains:
- **What** the concept is
- **Why** it exists
- **How** it works mathematically
- **Geometric intuition** (described visually)

If you understand this file, Logistic Regression will feel *inevitable*, not memorized.

---

## Q1. What problem does Logistic Regression solve?

**Answer (What):**  
Logistic Regression solves **binary classification** problems, where the target takes values 0 or 1.

**Why Linear Regression fails here:**  
Linear Regression predicts values on (−∞, +∞). But probabilities must lie in [0, 1].

**Key idea:**  
We don’t model the class directly. We model the **probability of belonging to class 1**.

---

## Q2. Is Logistic Regression really a regression model?

**Answer (What):**  
Despite its name, Logistic Regression is a **classification algorithm**.

**Why it is called regression:**  
Because it performs regression on the **log-odds** of the probability.

**Math intuition:**  
We regress:
log(p / (1 − p)) = wᵀx + b

---

## Q3. What is probability in Logistic Regression?

**Answer (What):**  
Probability represents the model’s confidence that y = 1.

**Math:**  
p(y = 1 | x) = σ(wᵀx + b)

where σ(z) = 1 / (1 + e⁻ᶻ)

**Why sigmoid:**  
It squashes any real number into (0, 1).

---

## Q4. Why do we model log-odds instead of probability directly?

**Answer (Why):**  
Probabilities are bounded, but log-odds are unbounded.

**Math:**  
Odds = p / (1 − p)
Log-odds = log(p / (1 − p)) ∈ (−∞, +∞)

This allows a **linear model** to operate naturally.

---

## Q5. What does a Logistic Regression model actually learn?

**Answer (What):**  
It learns a **linear decision boundary** in feature space.

**Geometric intuition:**  
Imagine a hyperplane separating two classes.  
The sigmoid only converts distance from this plane into probability.

---

## Q6. Why can’t we use Mean Squared Error for Logistic Regression?

**Answer (Why):**  
Because MSE leads to a **non-convex loss** with sigmoid.

**Consequence:**  
Multiple local minima → unstable optimization.

---

## Q7. What loss function does Logistic Regression use?

**Answer (What):**  
Binary Cross-Entropy (Log Loss).

**Math:**  
L = −[ y log(p) + (1 − y) log(1 − p) ]

**Why this loss:**  
It comes from Maximum Likelihood Estimation.

---

## Q8. How does Maximum Likelihood lead to log loss?

**Answer (How):**  
- Assume Bernoulli distribution for y
- Write likelihood of data
- Take log (for numerical stability)
- Minimize negative log-likelihood

This directly yields binary cross-entropy.

---

## Q9. Is Logistic Regression a probabilistic model?

**Answer:**  
Yes.

**Why:**  
It explicitly models p(y | x).

This is why it supports:
- Confidence scores
- Threshold tuning
- ROC / AUC analysis

---

## Q10. What does a coefficient mean in Logistic Regression?

**Answer (What):**  
A coefficient represents the change in **log-odds** for a unit change in the feature.

**Math:**  
Δ log-odds = wᵢ × Δxᵢ

**Important:**  
This is NOT a linear change in probability.

---

## Q11. Why are Logistic Regression coefficients hard to interpret?

**Answer (Why):**  
Because probability is a **non-linear function** of inputs.

Small coefficient changes can have large probability impact near decision boundary.

---

## Q12. What is the decision boundary in Logistic Regression?

**Answer (What):**  
The set of points where p(y=1|x) = 0.5.

**Math:**  
wᵀx + b = 0

**Key insight:**  
The boundary is linear, even though probabilities are non-linear.

---

## Q13. How does Logistic Regression handle class imbalance?

**Answer (How):**  
Poorly by default.

**Why:**  
Maximum likelihood favors majority class.

**Fixes:**  
- Class weights
- Threshold tuning
- Proper evaluation metrics

---

## Q14. Why is accuracy a bad metric for Logistic Regression?

**Answer (Why):**  
Because it ignores probability quality and class imbalance.

**Better metrics:**  
Precision, Recall, F1, ROC-AUC

---

## Q15. Is Logistic Regression a linear classifier?

**Answer:**  
Yes — in feature space.

**Clarification:**  
Non-linearity comes from probability mapping, not the decision boundary.

---

## Q16. How does regularization affect Logistic Regression?

**Answer (Why):**  
It controls coefficient magnitude to prevent overfitting.

**Math:**  
Loss + λ ||w||²  (L2)

---

## Q17. Why is there no closed-form solution for Logistic Regression?

**Answer (Why):**  
Because sigmoid makes the loss non-quadratic.

**Consequence:**  
We must use iterative optimization.

---

## Q18. What optimization methods are used?

**Answer:**  
- Gradient Descent
- Newton’s Method
- L-BFGS

---

## Q19. How is Logistic Regression related to Linear Regression?

**Answer:**  
Logistic Regression is Linear Regression applied to **log-odds**, not y.

---

## Q20. Biggest conceptual mistake people make with Logistic Regression?

**Answer:**  
Thinking it predicts classes instead of probabilities.

---

📌 **Next:** Mathematical derivation of Logistic Regression gradients and Hessian (with geometry).