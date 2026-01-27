# Decision Trees — Tricky Interview Questions (Deep Reasoning, Not Buzzwords)

This chapter covers **interview questions that expose shallow understanding of trees**. Each answer explains **what is really happening, why it happens, and how to reason it out**.

---

## Q1. If Decision Trees minimize impurity, why do they still overfit?

**What people say (wrong):**  
"Because trees are complex."

**Correct explanation:**  
Impurity is minimized **locally**, not globally.

**Why:**  
Greedy splits can isolate noise and create very pure leaves that do not generalize.

**Key idea:**  
Low impurity ≠ good generalization.

---

## Q2. Why doesn’t using entropy instead of Gini prevent overfitting?

**Why:**  
Both metrics rank splits similarly.

**Core reason:**  
Overfitting is caused by **depth and greediness**, not impurity choice.

---

## Q3. Why can two trees trained on almost identical data look very different?

**Why:**  
Small data changes alter early splits.

**Consequence:**  
Early splits define the entire subtree structure.

**Insight:**  
Trees are high-variance models.

---

## Q4. Why are Decision Trees considered unstable learners?

**Why:**  
They are sensitive to sampling noise.

**Geometric view:**  
Small perturbations → different partitions.

---

## Q5. Why do Decision Trees not need feature scaling?

**Why:**  
Splits depend only on feature ordering.

**Trap:**  
Confusing trees with distance-based models.

---

## Q6. Why do Decision Trees perform poorly on extrapolation tasks?

**Why:**  
Trees predict constant values in leaves.

**Contrast:**  
Linear models extrapolate; trees do not.

---

## Q7. Why do trees handle interactions naturally?

**Why:**  
Later splits are conditional on earlier ones.

**Interpretation:**  
Each path represents an interaction rule.

---

## Q8. Why does increasing depth always improve training accuracy?

**Why:**  
More splits → smaller regions → tighter fit.

**But:**  
Test performance eventually degrades.

---

## Q9. Why is max_depth a form of regularization?

**Why:**  
It limits model complexity.

**Analogy:**  
Like limiting polynomial degree.

---

## Q10. Why does pruning improve generalization?

**Why:**  
It removes branches that fit noise.

**Geometric view:**  
Merges small rectangles into larger ones.

---

## Q11. Why do trees prefer splits with many samples?

**Why:**  
Information Gain is weighted by node size.

**Effect:**  
Purifying many samples beats purifying few.

---

## Q12. Why does a tree sometimes split on a useless feature?

**Why:**  
Random fluctuations create apparent impurity reduction.

**Result:**  
Noise-driven splits.

---

## Q13. Why does adding noise features hurt trees badly?

**Why:**  
Greedy splitting may exploit noise.

**Contrast:**  
Linear models average noise; trees isolate it.

---

## Q14. Why do Decision Trees struggle with rotated decision boundaries?

**Why:**  
They only make axis-aligned splits.

**Effect:**  
Diagonal boundaries require many steps.

---

## Q15. Why do trees handle missing values poorly by default?

**Why:**  
Splitting assumes comparable values.

**Fixes:**  
- Surrogate splits
- Imputation

---

## Q16. Can a Decision Tree ever be unbiased?

**Answer:**  
Only in trivial cases.

**Reason:**  
Greedy heuristics introduce bias.

---

## Q17. Why are trees said to memorize data?

**Why:**  
Deep trees isolate individual samples.

**Effect:**  
Training error → zero.

---

## Q18. Why is interpretability of trees sometimes misleading?

**Why:**  
Many rules interact in deep trees.

**Reality:**  
Human-readable ≠ human-understandable.

---

## Q19. Why are single trees rarely used in production?

**Why:**  
High variance and instability.

**Preferred:**  
Ensembles.

---

## Q20. Biggest interview misconception about Decision Trees?

**Answer:**  
That they are simple and robust.

---

📌 **Next:** Real-world Decision Tree project issues — pruning