# 📘 DECISION TREES — A STORY OF QUESTIONS, CHOICES & PURITY

This notebook is written as a **story of decision-making**.

Read it like this:
> *A decision tree does not learn equations.  
It learns how to ask the **right questions in the right order**.*

---

## 1️⃣ WHY DECISION TREES EXIST (THE HUMAN ANALOGY)

Humans reason like this:
- If age > 40, then check BP
- If BP is high, then check cholesterol

We do **conditional questioning**.

Decision trees formalize this logic.

They:
- Split data
- Reduce uncertainty step by step
- Stop when decisions become clear

---

## 2️⃣ WHAT A DECISION TREE IS ACTUALLY DOING

At every node, the tree asks:
> *Which question should I ask now so that my uncertainty reduces the most?*

This uncertainty is called **impurity**.

---

## 3️⃣ WHAT IS IMPURITY (INTUITION FIRST)

- A pure node → all samples belong to one class
- An impure node → mixed classes

50–50 split = maximum confusion.

---

## 4️⃣ ENTROPY — UNCERTAINTY AS CONFUSION

### Intuition

Entropy measures:
> *How unsure am I before making a decision?*

If outcomes are equally likely, uncertainty is maximum.

---

### Formula

Entropy = − Σ pᵢ log₂ pᵢ

Where pᵢ is class probability.

---

### Example (step-by-step)

Dataset:
- 10 samples
- 6 Yes, 4 No

p(Yes)=0.6, p(No)=0.4

Entropy = −[0.6 log₂ 0.6 + 0.4 log₂ 0.4]

= −[0.6(−0.737) + 0.4(−1.322)]

= 0.97 (high uncertainty)

---

## 5️⃣ GINI IMPURITY — MISCLASSIFICATION VIEW

### Intuition

Imagine:
- You randomly pick a data point
- You randomly assign a class according to node distribution

Gini = probability of **misclassification**.

---

### How the formula comes

Probability of correct classification:

Σ pᵢ²

So probability of misclassification:

Gini = 1 − Σ pᵢ²

---

### Example

p(Yes)=0.9, p(No)=0.1

Correct classification = 0.9² + 0.1² = 0.82

Gini = 1 − 0.82 = 0.18

Low impurity.

---

## 6️⃣ INFORMATION GAIN — HOW SPLITS ARE CHOSEN

Information Gain =

Entropy(parent) − weighted entropy(children)

Tree chooses split with **maximum gain**.

---

## 7️⃣ FULL DATASET EXAMPLE (STEP-BY-STEP)

Dataset (Play Tennis):

| Outlook | Play |
|-------|------|
| Sunny | No |
| Sunny | No |
| Overcast | Yes |
| Rain | Yes |
| Rain | Yes |
| Rain | No |

Step 1: Compute parent entropy

Yes=3, No=3 → Entropy = 1

Step 2: Split on Outlook

Sunny → No, No → Entropy=0
Overcast → Yes → Entropy=0
Rain → Yes, Yes, No → Entropy=0.918

Step 3: Weighted entropy

= (2/6)*0 + (1/6)*0 + (3/6)*0.918 = 0.459

Information Gain = 1 − 0.459 = 0.541

---

## 8️⃣ DECISION TREE AS REGRESSOR

Instead of class labels:
- Leaves store mean value

Splits minimize:
- Variance
- Mean Squared Error

Tree predicts average of leaf.

---

## 9️⃣ WHY TREES OVERFIT

Trees keep splitting until:
- Zero impurity
- Memorization

This gives:
- Low bias
- High variance

---

## 🔟 REGULARIZATION IN DECISION TREES

Trees are regularized by **stopping growth**:

- max_depth
- min_samples_split
- min_samples_leaf
- max_features

This is pruning.

---

## 1️⃣1️⃣ PRE-PRUNING VS POST-PRUNING

- Pre-pruning: stop early
- Post-pruning: grow fully, then cut back

Goal:
> Balance bias and variance

---

## 🧠 100 INTERVIEW QUESTIONS (WITH ANSWERS)

### 🟢 Basic (1–20)
1. What is a decision tree?
→ A model that makes decisions via hierarchical splits.
2. What is a leaf node?
→ Final prediction node.
3. What is impurity?
→ Measure of class mixing.
4. Why is 50–50 most impure?
→ Maximum uncertainty.
5. What is entropy?
→ Measure of uncertainty.
6. Range of entropy?
→ 0 to 1.
7. What is Gini?
→ Probability of misclassification.
8. Range of Gini?
→ 0 to 0.5.
9. What is information gain?
→ Reduction in entropy.
10. Why do trees split greedily?
→ Global optimization is NP-hard.
11. What is root node?
→ First split.
12. What is depth?
→ Longest path from root to leaf.
13. Can trees handle categorical data?
→ Yes.
14. Can trees handle missing values?
→ Yes (with strategies).
15. Are trees scale-sensitive?
→ No.
16. Do trees need normalization?
→ No.
17. Are trees interpretable?
→ Yes.
18. Bias of trees?
→ Low.
19. Variance of trees?
→ High.
20. Main weakness?
→ Overfitting.

---

### 🟡 Intermediate (21–50)
21. Entropy vs Gini?
→ Similar splits, Gini faster.
22. Why Gini used more?
→ Computationally cheaper.
23. Can information gain be negative?
→ No.
24. Why trees overfit?
→ Keep splitting.
25. How to prevent overfitting?
→ Pruning.
26. What is min_samples_leaf?
→ Minimum samples per leaf.
27. What is max_depth?
→ Maximum depth allowed.
28. Why shallow trees generalize better?
→ Reduced variance.
29. What is decision tree regressor?
→ Predicts mean value.
30. How splits chosen in regression?
→ Minimize variance.
31. Why trees unstable?
→ Small data change → big structure change.
32. Why trees good baseline?
→ Interpretability.
33. Can trees extrapolate?
→ No.
34. What happens with noisy data?
→ Overfitting.
35. What is greedy splitting?
→ Local optimal choice.
36. Why global optimum not found?
→ Computationally infeasible.
37. Handling imbalance in trees?
→ Class weights.
38. Trees vs linear models?
→ Non-linear splits.
39. When to prefer trees?
→ Rule-based logic.
40. Feature importance in trees?
→ Based on impurity reduction.
41. Can trees handle interactions?
→ Yes, naturally.
42. Why entropy uses log?
→ Penalize uncertainty.
43. Gini vs misclassification error?
→ Gini smoother.
44. Why misclassification error not used?
→ Insensitive to changes.
45. What is CART?
→ Binary tree algorithm.
46. CART uses which impurity?
→ Gini.
47. ID3 uses which?
→ Entropy.
48. Can trees handle outliers?
→ Yes.
49. Are trees parametric?
→ No.
50. Why trees are high variance?
→ Data-driven splits.

---

### 🔴 Advanced & Scenario (51–100)
51. Why decision trees struggle with linear boundaries?
→ Axis-aligned splits.
52. Why ensemble trees?
→ Reduce variance.
53. Tree vs Random Forest?
→ Averaging trees.
54. Tree vs XGBoost?
→ Sequential error correction.
55. Why pruning improves test accuracy?
→ Removes noise-fitting splits.
56. Pre vs post pruning tradeoff?
→ Bias vs variance.
57. When use tree regressor?
→ Non-linear numeric targets.
58. Can trees overfit small data?
→ Yes.
59. What happens if max_depth = None?
→ Full memorization.
60. How trees handle missing values?
→ Surrogate splits.
61. Can trees learn monotonicity?
→ No.
62. Why trees are not smooth?
→ Piecewise constant predictions.
63. Why Gini = 1 − Σp²?
→ Misclassification probability.
64. Why entropy and gini give similar splits?
→ Both convex impurity measures.
65. Can trees be regularized via loss?
→ Indirectly.
66. Why trees bad for extrapolation?
→ Leaf averages.
67. How trees handle categorical splits?
→ One-vs-rest or grouping.
68. When trees beat linear models?
→ Strong non-linearity.
69. Tree depth vs interpretability?
→ Deeper = less interpretable.
70. How trees handle interactions?
→ Sequential splits.
71. Why tree splits are axis-aligned?
→ Computational simplicity.
72. What is cost-complexity pruning?
→ Penalize depth.
73. Can trees be probabilistic?
→ Yes (class proportions).
74. Why trees unstable to noise?
→ Greedy decisions.
75. Can trees handle multi-output?
→ Yes.
76. Why trees popular in industry?
→ Explainability.
77. How trees scale with data?
→ O(n log n).
78. Trees vs kNN?
→ Structured vs lazy.
79. Why not use entropy always?
→ Computational cost.
80. What is split criterion bias?
→ Favoring many-category features.
81. How to fix split bias?
→ Gain ratio.
82. What is gain ratio?
→ Normalized information gain.
83. Trees for time series?
→ With feature engineering.
84. Why trees memorize?
→ Exact thresholds.
85. Trees vs neural nets?
→ Interpretability vs flexibility.
86. What is monotonic constraint?
→ Feature monotonicity.
87. Why trees used in credit models?
→ Regulatory explainability.
88. Can trees learn XOR?
→ Yes.
89. Why trees good for tabular data?
→ Flexible splits.
90. What is leaf purity?
→ Homogeneity.
91. Why stopping early increases bias?
→ Less expressive.
92. How to choose max_depth?
→ Cross-validation.
93. Tree vs SVM?
→ Interpretability vs margin.
94. Can trees be smoothened?
→ Ensembles.
95. Why trees poor at ranking?
→ Hard splits.
96. Trees vs NB?
→ Rule-based vs probabilistic.
97. Trees vs Logistic?
→ Non-linear vs linear boundary.
98. Why trees handle mixed data?
→ No scaling required.
99. Biggest mistake using trees?
→ No pruning.
100. One sentence summary?
→ Trees learn decisions by reducing uncertainty step by step.

---

## ✅ DECISION TREE NOTEBOOK COMPLETE

Next logical step:
👉 **Random Forests & Ensemble Methods**

