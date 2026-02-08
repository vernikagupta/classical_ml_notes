# Logistic Regression — Mathematical Derivation (Deep, Step-by-Step)

This chapter derives Logistic Regression **from first principles** and explains **why each step exists**, **how the math works**, and **what the geometry means**.

> How to read this file: read the explanation first, then the equations. The equations are here to *confirm* intuition, not replace it.

---

## Q1. What random variable model do we assume for classification?

**What:**  
We assume the target y follows a **Bernoulli distribution**.

**Why:**  
Binary outcomes (0/1) are naturally modeled as Bernoulli trials.

**How (math):**  
P(y | x) = p^y (1 − p)^(1 − y), where p = P(y=1|x)

**Interpretation:**  
The model’s job is to estimate p given x.

---

## Q2. How do we connect features x to probability p?

**What:**  
We use a linear score z = wᵀx + b and map it to probability.

**Why:**  
Linear models are simple, stable, and interpretable in high dimensions.

**How (math):**  
p = σ(z) = 1 / (1 + e^(−z))

**Geometry:**  
z is the signed distance from a hyperplane; sigmoid converts distance → probability.

**Visual (external):**  
Sigmoid curve showing distance-to-probability mapping:
https://developers.google.com/machine-learning/crash-course/logistic-regression/sigmoid-function

---

## Q3. Why do we use Maximum Likelihood Estimation (MLE)?

**What:**  
We choose parameters that make the observed labels most probable.

**Why:**  
MLE provides a principled way to learn probabilistic models from data.

**How (math):**  
Likelihood:
L(w) = ∏ p_i^{y_i} (1 − p_i)^{1 − y_i}

---

## Q4. Why do we take the log of the likelihood?

**What:**  
We optimize the **log-likelihood** instead of likelihood.

**Why:**  
- Products become sums (numerically stable)
- Easier differentiation

**How (math):**  
log L(w) = Σ [ y_i log(p_i) + (1 − y_i) log(1 − p_i) ]

---

## Q5. How does log-likelihood become log loss?

**What:**  
Training Logistic Regression is equivalent to **minimizing negative log-likelihood**.

**Why:**  
Optimization frameworks minimize, not maximize.

**How (math):**  
Loss = −(1/n) Σ [ y_i log(p_i) + (1 − y_i) log(1 − p_i) ]

This is **Binary Cross-Entropy (Log Loss)**.

---

## Q6. Why is log loss the “right” loss for classification?

**Why:**  
- Penalizes confident wrong predictions heavily
- Encourages calibrated probabilities
- Leads to convex optimization

**Intuition:**  
Being confidently wrong should hurt more than being unsure.

---

## Q7. Why is there no closed-form solution?

**What:**  
Unlike Linear Regression, Logistic Regression has no normal equation.

**Why:**  
Sigmoid makes the loss **non-quadratic**.

**Consequence:**  
We must use iterative optimization.

---

## Q8. How do we compute the gradient of log loss?

**What:**  
We differentiate the loss w.r.t. weights.

**How (math):**  
∂L/∂w = (1/n) Xᵀ (p − y)

**Why this is elegant:**  
Same residual form as Linear Regression, but residual = (p − y).

---

## Q9. What does the gradient mean intuitively?

**Interpretation:**  
- If p > y → prediction too high → decrease weights
- If p < y → prediction too low → increase weights

This is **probability error correction**.

---

## Q10. What optimization methods are used and why?

**Gradient Descent:**  
- Scales well to large data
- Uses first-order information

**Newton / L-BFGS:**  
- Uses curvature (Hessian)
- Faster convergence for small–medium datasets

---

## Q11. What is the Hessian in Logistic Regression?

**What:**  
Matrix of second derivatives.

**How (math):**  
H = Xᵀ R X, where R is diagonal with p_i(1 − p_i)

**Interpretation:**  
Curvature depends on confidence of predictions.

---

## Q12. Why is Logistic Regression loss convex?

**Why:**  
- Sigmoid + log loss produces a bowl-shaped surface
- Hessian is positive semi-definite

**Consequence:**  
Single global minimum → stable training.

---

## Q13. How does regularization enter the math?

**What:**  
We penalize large weights.

**How (math):**  
L_reg = L + λ ||w||²

**Why:**  
Prevents extreme log-odds swings and overfitting.

---

## Q14. What does regularization do geometrically?

**Interpretation:**  
- Shrinks decision boundary toward origin
- Prevents boundary from twisting due to noise

---

## Q15. How is the decision boundary derived mathematically?

**What:**  
Boundary occurs at p = 0.5.

**How (math):**  
wᵀx + b = 0

**Key insight:**  
Even though probabilities are non-linear, the boundary is linear.

**Visual (external):**  
Decision boundary with probability contours:
https://python.plainenglish.io/logistic-regression-101-from-theory-to-practice-with-python-c51ddfaa4758#visualizing-decision-boundary

---

## Q16. Why does Logistic Regression output calibrated probabilities?

**Why:**  
MLE + proper scoring rule (log loss) encourages calibration.

**Interpretation:**  
Among linear classifiers, Logistic Regression is the most probabilistically honest.

---

## Q17. What is the mathematical relationship to Linear Regression?

**Connection:**  
Linear Regression minimizes squared error on y.

Logistic Regression minimizes log loss on **log-odds of y**.

Both are linear models at their core.

---

## Q18. When does Logistic Regression mathematically fail?

**Cases:**  
- Perfect class separation (weights blow up)
- Strong non-linearity without feature engineering

---

## Q19. Why do weights explode with perfect separation?

**Why:**  
Likelihood increases without bound as boundary margin increases.

**Fix:**  
Regularization.

---

## Q20. Mathematical takeaway

Logistic Regression is:
- Linear in parameters
- Probabilistic by design
- Convex and stable
- Interpretable in log-odds space

This is why it remains a gold standard baseline.

---

📌 **Next:** Geometric interpretation — probability contours, margins, and how coefficients reshape space.