# Logistic Regression — From Scores to Probabilities (A First-Principles Story)

> This document is written as a **conceptual story**, not a shortcut guide.
> A first-time learner can read this end-to-end to build intuition, while it remains deep enough for **interviews and real ML projects**.

---

## Table of Contents
1. Why Classification Is Different from Regression
2. The Core Idea: Predict Probability, Not Class
3. Linear Scores (Why Regression Still Appears)
4. Why We Need a Link Function
5. Sigmoid Function — Meaning, Not Just Formula
6. Odds and Log-Odds (The Central Assumption)
7. Probability vs Likelihood (Critical Distinction)
8. Maximum Likelihood Estimation (MLE)
9. Why MSE Comes from Gaussian Noise
10. Why Log Loss Comes from Bernoulli Outcomes
11. Why MSE Fails for Logistic Regression
12. Optimization and Infinite Weights Problem
13. Regularization in Logistic Regression
14. Assumptions of Logistic Regression
15. Metrics for Classification
16. Imbalanced Datasets and Real-World Handling
17. Practical Project Workflow
18. Interview Questions (Beginner → Advanced)

---

## 1. Why Classification Is Different from Regression

Regression problems ask:
> *How much?*

Classification problems ask:
> *Which one, and how confident are you?*

Predicting 0.51 and 0.99 both give class = 1, but they **do not mean the same thing**.

Confidence matters.

---

## 2. The Core Idea: Predict Probability, Not Class

Logistic regression separates two things:
- Learning → estimating probability
- Decision → applying a threshold

This makes the model flexible and interpretable.

---

## 3. Linear Scores — Why Regression Still Appears

We compute a score:

z = wᵀx + b

Interpretation:
- Each feature pushes confidence up or down
- z is **not** a probability

---

## 4. Why We Need a Link Function

We need a function that:
- Maps (−∞, +∞) → (0, 1)
- Is smooth and differentiable
- Is sensitive near decision boundary

Hard thresholds break learning.

---

## 5. Sigmoid Function — Meaning

Sigmoid:

p = 1 / (1 + e^(−z))

Properties:
- Smooth
- Saturates at extremes
- Steep near zero

This perfectly matches probability behavior.

---

## 6. Odds and Log-Odds (Core Assumption)

Odds:

odds = p / (1 − p)

Log-odds:

log(p / (1 − p)) = wᵀx + b

**Assumption:** Log-odds are linear in features.

---

## 7. Probability vs Likelihood

### Probability
- Parameters fixed
- Outcome uncertain

### Likelihood
- Outcome fixed
- Parameters uncertain

ML optimizes likelihood because data is already observed.

---

## 8. Maximum Likelihood Estimation (MLE)

MLE chooses parameters that make observed data most probable.

This principle unifies loss functions.

---

## 9. Why MSE Comes from Gaussian Noise

Assume:
- Errors follow a normal distribution

Maximizing likelihood leads to minimizing:

Σ (y − ŷ)²

So MSE is not arbitrary.

---

## 10. Why Log Loss Comes from Bernoulli Outcomes

Binary labels follow Bernoulli distribution:

P(y|p) = p^y (1 − p)^(1 − y)

Log-likelihood leads to:

Loss = −[y log p + (1 − y) log(1 − p)]

---

## 11. Why MSE Fails for Logistic Regression

MSE:
- Treats probability errors symmetrically
- Does not punish confident wrong predictions

Log loss explodes for confident mistakes.

Classification needs confidence-aware loss.

---

## 12. Optimization and Infinite Weights

For linearly separable data:
- Increasing weights increases confidence
- Log loss keeps decreasing

Result: weights grow infinitely.

---

## 13. Regularization in Logistic Regression

Regularization introduces two forces:

- Data-fit force
- Penalty force

### L2 (Ridge)
- Controls confidence
- Stabilizes solution

### L1 (Lasso)
- Can zero out features

---

## 14. Assumptions of Logistic Regression

1. Log-odds linearity
2. Independent observations
3. No severe multicollinearity
4. Correct link function

---

## 15. Metrics for Classification

- Accuracy (misleading for imbalance)
- Precision
- Recall
- F1-score
- ROC-AUC

---

## 16. Imbalanced Datasets (Real World)

### Undersampling
- Remove majority samples
- Use when data is huge

### Oversampling
- Duplicate minority samples
- Risk overfitting

### SMOTE
- Synthetic samples
- Use with caution

---

## 17. Practical Project Workflow

1. Baseline model
2. Choose correct metric
3. Handle imbalance
4. Regularize
5. Tune threshold

---

## 18. Interview Questions (Selected)

**Q. Why logistic regression is linear but non-linear?**  
Linear in parameters, non-linear in output.

**Q. Why log loss is preferred?**  
Penalizes confident wrong predictions.

**Q. When recall is more important than precision?**  
When false negatives are costly.

---

## One-Line Summary

> Logistic regression models probability using linear log-odds and is trained via likelihood, not squared error.

