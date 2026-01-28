# Boosting — AdaBoost, Gradient Boosting & Geometry of Bias Reduction

> This chapter is **math-complete first**, intuition-rich second.  
> Focus: *why boosting exists*, *what problem it fixes (bias)*, and *how math + geometry explain its behavior*.

---

## 1. Why Random Forest Is Not the End

From the Random Forest chapter:
- RF dramatically reduces **variance**
- RF does **not** aggressively reduce **bias**

When the true decision boundary is:
- Complex
- Curved
- Requires many rectangles

Averaging many trees still leaves **systematic error**.

Boosting addresses:

> **Bias — the error due to underfitting**.

---

## 2. Core Idea of Boosting (One Sentence)

> **Train models sequentially so that each new model focuses on the mistakes of the previous ones.**

This is fundamentally different from bagging:
- Bagging → parallel, independent
- Boosting → sequential, dependent

---

## 3. Weak Learners (Formal Definition)

A weak learner is a model that performs:

Error < 0.5  (binary classification)

Decision stumps (depth-1 trees) are typical weak learners:
- Very high bias
- Very low variance

Boosting converts:

> Many weak learners → one strong learner

---

## 4. AdaBoost — Formal Setup

Given:
- Training data (xᵢ, yᵢ)
- yᵢ ∈ {−1, +1}

Initialize weights:

wᵢ = 1/n

Train weak learner h₁(x).

---

## 5. Weighted Error (Exact Formula)

Weighted error:

εₜ = ∑ᵢ wᵢ · 𝟙(hₜ(xᵢ) ≠ yᵢ)

Constraint:

εₜ < 0.5

---

## 6. Learner Weight (Why This Formula)

AdaBoost assigns:

αₜ = 1/2 · ln((1 − εₜ)/εₜ)

Meaning:
- Better learner → larger α
- Worse learner → smaller α

This emerges from **loss minimization**, not heuristics.

---

## 7. Weight Update Rule (Derivation Outcome)

Update sample weights:

wᵢ ← wᵢ · exp(−αₜ yᵢ hₜ(xᵢ))

Interpretation:
- Misclassified → weight increases
- Correct → weight decreases

Then normalize.

---

## 8. Final AdaBoost Model

Final classifier:

F(x) = sign( ∑ₜ αₜ hₜ(x) )

This is an **additive model**.

---

## 9. Loss Function Behind AdaBoost (Very Important)

AdaBoost minimizes **exponential loss**:

L(y, F(x)) = exp(−yF(x))

Key properties:
- Strongly penalizes confident mistakes
- Emphasizes hard points

---

## 10. Margin Theory (Geometry)

Margin:

mᵢ = yᵢ F(xᵢ)

Boosting:
- Increases minimum margin
- Even if training error is already zero

This explains:
- Good generalization
- Resistance to overfitting early

---

## 11. Why AdaBoost Works (Bias View)

Each stump:
- Very biased

Sequential correction:
- Reduces systematic error
- Builds complex boundary step-by-step

Boosting fits:

> Residual structure

---

## 12. Geometry of Boosting

Each weak learner adds:
- A small correction in function space

Overall model:

F(x) = F₀(x) + ∑ₜ αₜ hₜ(x)

This is **functional addition**, not parameter averaging.

---

## 13. From AdaBoost to Gradient Boosting

AdaBoost is a special case of:

> **Gradient Descent in Function Space**

Instead of parameters, we optimize:

F(x)

---

## 14. Gradient Boosting — Formal Objective

Minimize:

∑ᵢ L(yᵢ, F(xᵢ))

Iterative update:

Fₜ(x) = Fₜ₋₁(x) + η hₜ(x)

Where hₜ fits:

− ∂L/∂F |_{Fₜ₋₁}

---

## 15. Squared Loss Example (Regression)

Loss:

L = (y − F(x))²

Negative gradient:

rᵢ = yᵢ − F(xᵢ)

So:
- Each tree fits residuals

---

## 16. Logistic Loss Example (Classification)

Loss:

L = log(1 + exp(−yF(x)))

Gradient:

rᵢ = yᵢ − σ(F(xᵢ))

Boosting fits **pseudo-residuals**.

---

## 17. Learning Rate (Shrinkage)

Small η:
- Slower learning
- Better generalization

This controls:
- Bias–variance tradeoff

---

## 18. Overfitting in Boosting (When It Happens)

Boosting can overfit when:
- Noisy labels
- Large trees
- Large learning rate

Boosting is **not immune**.

---

## 19. Comparison: Bagging vs Boosting

| Aspect | Bagging | Boosting |
|------|--------|----------|
| Training | Parallel | Sequential |
| Fixes | Variance | Bias |
| Correlation | Reduced by randomness | Not required |
| Geometry | Averaging | Additive correction |

---

## 20. Intuition Recap (For Non-Statistical Readers)

- Bagging asks many independent opinions
- Boosting listens to mistakes and corrects them
- Each step focuses where model is weak

---

## 21. Bridge Forward

Boosting leads to:
- Gradient Boosting Machines (GBM)
- XGBoost, LightGBM, CatBoost

Next chapter:

> **XGBoost — Regularization, Second-Order Geometry & Practical Power**

---

*This chapter completes the ensemble foundations: Trees → RF → Boosting.*

