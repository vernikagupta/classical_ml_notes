# Decision Trees — Impurity & Splitting (Math, Intuition, and Why It Works)

This chapter explains **why Decision Trees split the way they do**. We will go deep into:
- What impurity really measures
- Why Gini and Entropy exist
- How Information Gain is computed
- Why greedy splitting works surprisingly well

Every section answers **what**, **why**, and **how**, with math and intuition.

---

## Q1. What is impurity in a Decision Tree?

**What:**  
Impurity measures how **mixed** the labels are at a node.

**Intuition:**  
- Pure node → mostly one class
- Impure node → many classes mixed

**Why impurity matters:**  
A pure node makes confident predictions.

---

## Q2. Why do trees aim to reduce impurity?

**Why:**  
Reducing impurity makes child nodes more predictable than the parent.

**Key idea:**  
A good split increases information about the target.

---

## Q3. What are the common impurity measures?

**Classification:**  
- Gini Impurity
- Entropy

**Regression:**  
- Variance
- Mean Squared Error

---

## Q4. What is Gini Impurity?

**What (definition):**  
Gini measures the probability of misclassification if labels are randomly assigned according to class proportions.

**Math:**  
Gini = 1 − Σ pᵢ²

where pᵢ is the fraction of class i at the node.

---

## Q5. Why does Gini use squared probabilities?

**Why:**  
Squaring emphasizes dominant classes.

**Intuition:**  
If one class dominates, pᵢ² is large → impurity is low.

---

## Q6. What are the extreme values of Gini?

**Pure node:**  
Gini = 0

**Maximum impurity (binary):**  
Gini = 0.5 when p = 0.5

---

## Q7. What is Entropy?

**What (definition):**  
Entropy measures the **uncertainty** in class labels.

**Math:**  
Entropy = − Σ pᵢ log(pᵢ)

---

## Q8. Why is entropy linked to information theory?

**Why:**  
Entropy quantifies expected information (surprise).

**Interpretation:**  
More mixed labels → more uncertainty → higher entropy.

---

## Q9. What are the extreme values of Entropy?

**Pure node:**  
Entropy = 0

**Maximum (binary):**  
Entropy = 1 when p = 0.5

---

## Q10. How do Gini and Entropy differ intuitively?

**Gini:**  
- Faster to compute
- Slightly favors larger partitions

**Entropy:**  
- More sensitive to class distribution changes
- Stronger penalty for mixed nodes

---

## Q11. Why do Gini and Entropy often give similar trees?

**Why:**  
Both are monotonic functions of class proportions.

**Key insight:**  
They rank splits similarly in practice.

---

## Q12. What is Information Gain?

**What:**  
Information Gain measures impurity reduction after a split.

**Math:**  
IG = Impurity(parent) − Σ (n_child / n_parent) · Impurity(child)

---

## Q13. Why do we weight child impurities?

**Why:**  
Larger child nodes should matter more.

**Interpretation:**  
A split that purifies many points is better than one that purifies a few.

---

## Q14. How does a tree choose the best split?

**How:**  
Evaluate all candidate splits and pick the one with maximum Information Gain.

**Greedy nature:**  
Only current split is optimized.

---

## Q15. Why is greedy splitting not globally optimal?

**Why:**  
Early splits constrain later choices.

**But:**  
Greedy works well in practice due to exponential search space.

---

## Q16. How do trees handle continuous features during splitting?

**How:**  
- Sort feature values
- Try midpoints between unique values

**Cost:**  
Computationally expensive

---

## Q17. What impurity measure is used for regression trees?

**Answer:**  
Variance or Mean Squared Error.

**Why:**  
We want child nodes with tight target distributions.

---

## Q18. How does variance reduction work?

**Math:**  
Variance = (1/n) Σ (yᵢ − ȳ)²

**Split goal:**  
Reduce weighted variance after split.

---

## Q19. Why does impurity reduction correspond to better predictions?

**Why:**  
Lower impurity → less uncertainty in predictions.

**Interpretation:**  
Leaves approximate conditional distributions.

---

## Q20. Why can trees still overfit even with impurity-based splits?

**Why:**  
Greedy splits can isolate noise.

**Result:**  
Pure leaves with poor generalization.

---

## Q21. Visual intuition (highly recommended)

- Gini vs Entropy plots:
https://towardsdatascience.com/gini-impurity-and-entropy-what-are-they-and-how-are-they-used-in-decision-trees-9d66fdc4f2b

- Information Gain visualization:
https://www.analyticsvidhya.com/blog/2020/06/decision-tree-splitting-criteria-explained/

---

## Q22. Key takeaway

Impurity measures are:
- Local heuristics
- Information-theoretic
- Computationally efficient

They explain **why trees split**, but not **when they should stop**.

---

📌 **Next:** Geometric interpretation of Decision Trees — axis-aligned partitions and why trees look blocky.