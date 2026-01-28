# Decision Trees — Intuition, Geometry, Information & Bias–Variance

> Written for **non-statisticians and engineers first**, without losing rigor.  
> Goal: understand *why trees work*, *why they overfit*, and *why ensembles are needed*.

---

## 1. Why We Need Decision Trees (What Linear Models Cannot Do)

Linear and logistic regression:
- Draw straight boundaries
- Combine features additively

But many real-world rules look like:
- *If age > 30 AND income < X AND city = Y*
- *If pixel region A is bright AND region B is dark*

These are **conditional rules**, not smooth trends.

Decision trees model **logic**, not equations.

---

## 2. What a Decision Tree Really Is (Plain Language)

A decision tree is:
- A sequence of **yes/no questions**
- Asked in a **specific order**
- Each question reduces uncertainty

Example:
- Is age > 35?
- Is income > 10L?
- Is city = Bangalore?

At the end → make a decision.

---

## 3. Geometry of a Decision Tree (Very Important)

Decision trees **do not rotate space**.

They:
- Cut one feature at a time
- Always use **axis-aligned splits**

Geometrically:
- Space is divided into rectangles (2D)
- Boxes (3D)
- Hyper-rectangles (high-D)

This is why trees:
- Handle nonlinearity
- But struggle with diagonal boundaries

---

## 4. Why Trees Feel Intuitive to Humans

Humans think in rules:
- If this, then that
- Otherwise, something else

Trees mimic:
- Flowcharts
- Checklists
- Decision processes

This is why trees are:
- Interpretable
- Explainable
- Easy to debug

---

## 5. How Does a Tree Decide Where to Split?

At each node, the tree asks:

> "Which question reduces uncertainty the most?"

This is quantified using **impurity measures**.

---

## 6. Classification Trees — Impurity Intuition

Imagine a node with mixed classes.

Pure node:
- All samples same class

Impure node:
- Mixed classes

Goal:
- Split data so children are **more pure** than parent

---

## 7. Entropy (Information View)

Entropy measures **uncertainty**.

For binary classification:

Entropy = −p log p − (1−p) log(1−p)

Meaning:
- High entropy → confusion
- Low entropy → certainty

---

## 8. Information Gain (Why a Split Is Good)

Information Gain:

Gain = Parent Entropy − Weighted Child Entropy

Interpretation:
- How much uncertainty is reduced
- How much information is gained

Tree greedily picks:
- Split with maximum gain

---

## 9. Gini Impurity (Probability View)

Gini measures:

Probability of misclassification if we guess randomly

Gini = 1 − ∑ pₖ²

Properties:
- Faster to compute
- Similar behavior to entropy

That’s why CART uses Gini.

---

## 10. Regression Trees (Very Intuitive)

For regression, target is continuous.

Tree splits to:
- Reduce variance

Criterion:

MSE = ∑(yᵢ − mean(node))²

Leaves predict:
- Average of points in region

---

## 11. Trees Are Greedy (And Why That Matters)

Trees:
- Choose best split *now*
- Do not reconsider later

This means:
- Locally optimal
- Not globally optimal

But:
- Exhaustive search is impossible

---

## 12. Why Trees Overfit (Critical Insight)

Trees can:
- Keep splitting until pure
- Memorize noise

Geometrically:
- Tiny boxes around points
- Zero training error
- Poor generalization

Trees have:
- Low bias
- Very high variance

---

## 13. Bias–Variance Explained Without Math

Bias:
- Error from overly simple rules

Variance:
- Error from sensitivity to data changes

Trees:
- Extremely flexible
- Very sensitive

Hence:
- Low bias
- High variance

---

## 14. Why Pruning Helps

Pruning:
- Stops growth early
- Removes weak splits

Effect:
- Larger regions
- Smoother decisions
- Better generalization

Trade-off:
- Slight bias increase
- Large variance reduction

---

## 15. Trees vs Linear Models (Big Contrast)

| Aspect | Linear / Logistic | Decision Tree |
|------|------------------|---------------|
| Boundary | Smooth | Step-like |
| Geometry | Rotations | Axis-aligned |
| Interpretability | Medium | Very high |
| Variance | Low | High |

---

## 16. Why Trees Are Rarely Used Alone

Single trees:
- Unstable
- Sensitive to noise

Small data change → very different tree.

This motivates:
- Random Forests
- Boosting

---

## 17. Mental Model (Non-Technical)

Think of a decision tree as:

> A very detailed checklist.

More questions → more detail → more overfitting.

---

## 18. Bridge Forward

To fix variance:
- Average many trees → Random Forest

To fix bias + variance:
- Correct mistakes sequentially → Boosting

Trees are not weak — they are **unstable**.

---

*Next: Random Forests — why averaging chaos creates stability.*


---

# Appendix A — Mathematical Foundations of Decision Trees (Not Skipped)

> This appendix ensures the chapter is **mathematically complete**.  
> Intuition comes *after* math — not instead of it.

---

## A1. Formal Problem Setup

Dataset:
- X ∈ ℝⁿˣᵈ
- y ∈ {1,2,…,K} (classification)
- y ∈ ℝ (regression)

A decision tree represents a function:

f(x) = ∑ₗ cₗ · 𝟙(x ∈ Rₗ)

Where:
- Rₗ are disjoint regions (rectangles)
- cₗ is class label or mean value

---

## A2. Axis-Aligned Split (Mathematical Definition)

A split is defined by:

xⱼ ≤ t  or  xⱼ > t

This partitions region R into:

R_left = {x ∈ R | xⱼ ≤ t}
R_right = {x ∈ R | xⱼ > t}

Only **one coordinate** is used.

This is the core geometric restriction of trees.

---

## A3. Entropy (Exact Formula)

For a node with class probabilities p₁,…,p_K:

H = − ∑ₖ pₖ log pₖ

Properties:
- H ≥ 0
- H = 0 ⇔ node is pure
- Maximum when classes are uniform

---

## A4. Information Gain (Derivation)

Parent entropy:

H_parent

Children entropies:

H_left, H_right

Weighted entropy after split:

H_after = (n_L/n) H_left + (n_R/n) H_right

Information Gain:

IG = H_parent − H_after

Greedy split:

(j*, t*) = argmax IG(j,t)

---

## A5. Gini Impurity (Probability Interpretation)

Definition:

G = 1 − ∑ₖ pₖ²

Why this form?

Randomly guess class according to pₖ:
- Probability of correct = ∑ pₖ²
- Probability of error = 1 − ∑ pₖ²

So Gini = **expected misclassification probability**.

---

## A6. Regression Trees — Variance Reduction

At node R:

Prediction:

c_R = mean(yᵢ ∈ R)

Loss:

RSS = ∑_{i∈R} (yᵢ − c_R)²

Best split minimizes:

RSS_left + RSS_right

Equivalent to:
- Maximizing variance reduction

---

## A7. Greedy Nature (Formal Limitation)

Tree optimization solves:

min over all partitions of ℝᵈ

This is NP-hard.

Greedy splitting is a **tractable approximation**.

---

## A8. Bias–Variance (Formal View)

Expected error:

E[(y − f̂(x))²] = Bias² + Variance + Noise

Decision trees:
- Bias ≈ 0 (very flexible)
- Variance ≫ large

Reason:

Small data perturbation → different splits → different regions

---

## A9. Why Pruning Works (Mathematically)

Cost-complexity pruning minimizes:

R(T) + α|T|

Where:
- R(T) = training error
- |T| = number of leaves

α controls bias–variance tradeoff.

---

## A10. Geometric Summary (Formal)

- Trees partition ℝᵈ into rectangles
- No rotation of axes
- Piecewise-constant approximation

Formally:

f(x) = ∑ cₗ · 𝟙(x ∈ Rₗ)

This is why:
- Trees approximate any function
- But require many regions for smooth boundaries

---

# Appendix B — Intuition Recap (For Non-Statistical Readers)

- Trees ask one question at a time
- Each question reduces uncertainty
- Too many questions memorize data
- Averaging trees fixes instability

---

*This chapter is now mathematically complete, geometrically precise, and intuitively accessible.*

