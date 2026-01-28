# Logistic Regression — Geometry, Probability, Optimization

> This document is intentionally written in the **same depth, tone, and geometric intuition** as the Linear Regression notes.
> Nothing here is a shortcut explanation. Every step answers **what changes, how it changes, and why it must change**.

---

## 1. Why Linear Regression Fails for Classification (First Principles)

Linear Regression assumes:
- Target \( y \in \mathbb{R} \)
- Errors are **Gaussian**
- We are estimating a **conditional mean**

But in classification:
- \( y \in \{0,1\} \)
- There is **no meaningful mean** between classes
- Noise is **Bernoulli**, not Gaussian

Using squared loss forces:
- Predictions outside \([0,1]\)
- Misaligned gradients near class boundaries
- Poor probabilistic interpretation

👉 **So the failure is not algorithmic — it is statistical and geometric.**

---

## 2. What Logistic Regression Changes (and What It Does NOT)

**What stays the same**:
- Linear score: \( z = X\beta \)
- Same hyperplane geometry
- Same feature space

**What changes**:
- Interpretation of \( X\beta \)
- Loss function
- Noise model

Logistic regression does **not** predict class directly.
It predicts **log-odds**.

---

## 3. Log-Odds: The Correct Quantity to Model

Define probability:

\[ p = P(y=1|x) \]

Odds:

\[ \text{odds} = \frac{p}{1-p} \]

Log-odds:

\[ \log\frac{p}{1-p} = X\beta \]

Why log-odds?
- Unbounded → matches linear output
- Additive → aligns with linear geometry
- Invertible → gives probability back

---

## 4. Sigmoid Is Not Arbitrary

Solving for \( p \):

\[ p = \sigma(X\beta) = \frac{1}{1+e^{-X\beta}} \]

Sigmoid emerges as:
- Inverse of log-odds
- Mapping from \( \mathbb{R} \to (0,1) \)
- Smooth, monotonic probability surface

👉 **Sigmoid is forced by probability theory, not design choice.**

---

## 5. Geometry of the Decision Boundary

Decision rule:

\[ P(y=1|x) > 0.5 \iff X\beta > 0 \]

So:
- Boundary is still a **hyperplane**
- Same orientation as linear regression

But:
- Confidence saturates away from boundary
- Points far away contribute less to gradient

---

## 6. Correct Loss: Bernoulli Likelihood

Bernoulli likelihood:

\[ P(y|x) = p^y(1-p)^{1-y} \]

Negative log-likelihood:

\[ \mathcal{L}(\beta) = -\sum [y\log p + (1-y)\log(1-p)] \]

This is **cross-entropy loss**.

Why squared loss fails:
- Wrong noise model
- Wrong curvature
- Wrong gradient emphasis

---

## 7. Loss Geometry in Parameter Space

Loss:

\[ J(\beta) = \sum \log(1+e^{-yX\beta}) \]

Properties:
- Convex
- Smooth
- No closed-form minimizer

Contours:
- Elliptical near optimum
- Flatten in saturated regions

---

## 8. Gradient: Why Some Points Matter More

Gradient:

\[ \nabla J = X^T(\sigma(X\beta)-y) \]

Interpretation:
- Misclassified points → large gradient
- Confident correct points → near zero gradient

👉 Logistic regression **focuses learning near boundary**.

---

## 9. Hessian and Curvature

Hessian:

\[ H = X^T W X \]

Where:

\[ W = \text{diag}(p_i(1-p_i)) \]

Geometry:
- Points near boundary contribute most curvature
- Saturated points flatten loss

---

## 10. Why No Closed-Form Solution Exists

In linear regression:
- Quadratic loss
- Constant Hessian

In logistic regression:
- Curvature depends on \( \beta \)
- Hessian changes every step

So:

\[ \nabla J = 0 \]

cannot be solved analytically.

---

## 11. Newton, IRLS, Gradient Descent (As Consequences)

Newton update:

\[ \beta_{t+1} = \beta_t - H^{-1}\nabla J \]

This leads to **IRLS**.

But:
- Hessian can be ill-conditioned
- Inversion unstable

Hence:
- Gradient Descent
- Stochastic Gradient Descent

---

## 12. Regularization: Geometry Again

Add L2:

\[ J(\beta) + \lambda ||\beta||^2 \]

Effects:
- Adds curvature in flat directions
- Prevents coefficient explosion
- Stabilizes inversion

---

## 13. Final Mental Model

> Linear Regression fits a **mean**.
> Logistic Regression fits **log-odds**.

> Hyperplane geometry stays the same.
> Loss geometry fundamentally changes.

This is why logistic regression is:
- A probabilistic model
- A convex optimizer
- A shallow neural network

---

## 14. Bridge Forward

Logistic Regression naturally leads to:
- Softmax (multiclass)
- Neural networks
- Maximum entropy models

This is not an endpoint — it is the gateway.


---

# Softmax Regression, Neural View, Maximum Entropy & Calibration

> This section is written so that **even a non-statistics / non-ML engineer** can follow the logic.
> Math is used only when it *explains something real*.

---

## 15. From Logistic to Softmax (Why Binary Is Not Enough)

Logistic regression answers only one question:

> "Is this class 1 or not?"

But real problems ask:
- Which digit is this? (0–9)
- Which product category?
- Which disease?

Binary logic breaks down.

We need:
- Probabilities over **multiple classes**
- Probabilities that **sum to 1**

---

## 16. What Softmax Actually Does (Intuition First)

For each class k, compute a score:

zₖ = xᵀβₖ

These are **raw scores**, not probabilities.

Softmax converts scores into probabilities:

pₖ = exp(zₖ) / ∑ⱼ exp(zⱼ)

Plain-English meaning:
- Bigger score → exponentially more confident
- All probabilities normalized to sum to 1

---

## 17. Why Exponentials Are Necessary

Why not linear normalization?

Because we need:
1. Positivity (no negative probability)
2. Order preservation
3. Smooth gradients

Exponentials guarantee all three.

Softmax is the **only smooth way** to turn arbitrary scores into probabilities.

---

## 18. Geometry of Softmax Decision Boundaries

Decision rule:

Choose class with max score:

argmaxₖ xᵀβₖ

Between any two classes i and j:

xᵀβᵢ = xᵀβⱼ

This is still a **hyperplane**.

So:
- Boundaries are linear
- Probability surfaces are curved

---

## 19. Loss Function — Multiclass Cross-Entropy

Loss for one example:

L = − ∑ₖ yₖ log(pₖ)

Where yₖ is one-hot encoded.

Interpretation:
- Reward high probability on correct class
- Punish confident wrong predictions heavily

---

## 20. Logistic & Softmax as Neural Networks (Key Insight)

Logistic regression **is a neural network**:

- Inputs → weighted sum → sigmoid

Softmax regression:

- Inputs → weighted sums → softmax

This is a:
- Single-layer
- No hidden units
- Fully interpretable network

Deep learning simply **adds hidden layers**.

---

## 21. Why Neural Networks Need Nonlinearity

If we stack linear layers:

Linear → Linear → Linear

Result:
- Still linear

Nonlinearity (ReLU, sigmoid) bends space.

Without it:
- No curves
- No hierarchy
- No abstraction

---

## 22. Maximum Entropy View (Very Important, Very Intuitive)

Maximum Entropy principle says:

> "Among all models that fit the data, choose the least confident one."

Logistic regression is the **maximum entropy** model under:
- Linear constraints

Meaning:
- Do not assume extra structure
- Only trust what data enforces

This is why logistic regression:
- Generalizes well
- Avoids overconfidence

---

## 23. Why Regularization Fits Naturally Here

Regularization says:

> "Do not be overly confident without evidence."

L2 regularization:
- Penalizes sharp probability jumps
- Smooths decision boundary

Geometrically:
- Prevents extreme curvature

---

## 24. Probability vs Decision (Very Practical)

Model outputs:

P(y=k|x)

But final decision may depend on:
- Business cost
- Risk tolerance
- Class imbalance

Thresholding is **not learning**.
It is **policy**.

---

## 25. Calibration — Do Probabilities Mean What They Say?

A calibrated model:

> Among all predictions of 0.8, ~80% are correct.

Logistic regression is **naturally well-calibrated**.

Tree models often are not.

---

## 26. Why Calibration Matters (Real World)

Examples:
- Medical diagnosis
- Credit approval
- Fraud detection

Wrong probabilities → wrong decisions.

Accuracy alone is not enough.

---

## 27. Calibration Methods (Conceptual)

- Platt Scaling
- Isotonic Regression

They adjust probabilities **without changing boundaries**.

---

## 28. One Unified Mental Model (For Everyone)

Think like this:

- Linear Regression → predict *how much*
- Logistic Regression → predict *how likely*
- Softmax → distribute belief across choices
- Neural Networks → stack transformations

All are:
- Geometry
- Probability
- Optimization

---

## 29. Final Closure (Non-Technical Version)

Logistic & Softmax regression:
- Draw lines between groups
- Measure confidence smoothly
- Avoid overconfidence

They are simple, powerful, and still used everywhere.

---

*This completes the Logistic Regression chapter in a way accessible to non-statisticians and engineers alike.*

