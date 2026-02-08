# Decision Trees — Basics (How Trees Think, Split, and Overfit)

Decision Trees are often taught as simple models, but they hide **deep ideas about greedy optimization, structure-based regularization, and geometry**.

This chapter explains:
- **What a tree actually learns**
- **Why trees are powerful but dangerous**
- **How splitting really works (conceptually)**
- **Why trees overfit so easily**

---

## Q1. What problem do Decision Trees solve?

**What:**  
Decision Trees solve both **classification and regression** problems.

**Why they are different:**  
Instead of learning weights, trees learn **rules**.

**Mental model:**  
“If feature A ≤ threshold, go left; else go right.”

---

## Q2. What does a Decision Tree actually learn?

**What:**  
A Decision Tree learns a **set of hierarchical if–else rules**.

**Why this matters:**  
The model is not linear and not smooth.

**Key insight:**  
The structure *is* the model.

---

## Q3. How does a Decision Tree make predictions?

**How:**  
1. Start at the root
2. Follow splits based on feature values
3. Reach a leaf
4. Output the leaf’s prediction

**Classification:**  
Majority class or class probability

**Regression:**  
Mean target value in the leaf

---

## Q4. Why are Decision Trees considered non-parametric models?

**Why:**  
They do not assume a fixed functional form.

**Consequence:**  
Model complexity grows with data.

---

## Q5. What is a split in a Decision Tree?

**What:**  
A split divides data based on a **feature threshold**.

**Example:**  
Age ≤ 35 vs Age > 35

---

## Q6. How does the tree decide where to split?

**Core idea:**  
Choose the split that produces the **purest children**.

**Purity:**  
How homogeneous the labels are after splitting.

---

## Q7. What is a node and what is a leaf?

**Node:**  
A point where data is split.

**Leaf:**  
A terminal node with a prediction.

---

## Q8. Why are trees called greedy models?

**Why:**  
Each split is chosen to be locally optimal.

**Important:**  
The tree does not reconsider past splits.

---

## Q9. Why can greedy splitting be dangerous?

**Why:**  
A locally optimal split may not lead to a globally optimal tree.

**Consequence:**  
Early mistakes propagate downward.

---

## Q10. Why do Decision Trees overfit so easily?

**Why:**  
They can keep splitting until each leaf has very few points.

**Extreme case:**  
One sample per leaf → zero training error.

---

## Q11. What does overfitting look like in a tree?

**Symptoms:**  
- Very deep tree
- Many leaves
- Perfect training accuracy
- Poor test performance

---

## Q12. How do Decision Trees handle non-linear relationships?

**Why well:**  
They partition space instead of fitting curves.

**Interpretation:**  
Piecewise constant approximation.

---

## Q13. How do trees handle feature interactions?

**Naturally:**  
Splits at deeper levels automatically encode interactions.

**Example:**  
Age split followed by Income split.

---

## Q14. Are Decision Trees sensitive to feature scaling?

**Answer:**  
No.

**Why:**  
Splits depend on ordering, not magnitude.

---

## Q15. How do trees handle categorical variables?

**How:**  
- One-vs-rest splits
- Subset splits (in theory)

**Note:**  
Many libraries restrict split types for efficiency.

---

## Q16. What assumptions do Decision Trees make?

**Minimal assumptions:**  
- No linearity assumption
- No distributional assumption

**Cost:**  
High variance.

---

## Q17. What is the bias–variance profile of trees?

**Profile:**  
- Low bias
- High variance

This explains why single trees rarely generalize well.

---

## Q18. Why are trees unstable models?

**Why:**  
Small data changes can lead to different splits.

**Consequence:**  
Different trees from similar data.

---

## Q19. Why are trees interpretable but misleading?

**Why:**  
Rules are human-readable.

**But:**  
Deep trees become incomprehensible.

---

## Q20. When should you use a single Decision Tree?

**Use cases:**  
- Small datasets
- Need for transparency
- Baseline models

---

## Q21. Biggest misconception about Decision Trees?

**Answer:**  
That they are "simple" models.

---

📌 **Next:** Impurity measures (Gini, Entropy) — math, intuition, and why splits work.

