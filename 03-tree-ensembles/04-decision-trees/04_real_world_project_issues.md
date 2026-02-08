# Decision Trees — Real-World Project Issues (Why Single Trees Rarely Survive Production)

This chapter explains **how Decision Trees behave in real ML projects**, why they are rarely deployed alone, and what experienced teams watch out for.

Each section answers:
- **What goes wrong in practice**
- **Why it goes wrong**
- **How professionals handle it**

---

## Q1. Why are single Decision Trees rarely used in production?

**Short answer:**  
They are unstable.

**Why:**  
Small changes in data lead to different early splits, which completely change the tree structure.

**Consequence:**  
Predictions fluctuate across retraining cycles.

---

## Q2. Why is tree interpretability often overstated?

**What people assume:**  
Trees are easy to interpret.

**Reality:**  
- Shallow trees are interpretable
- Deep trees are not

**Problem:**  
Hundreds of rules interact non-trivially.

---

## Q3. How do stakeholders misunderstand tree rules?

**Why:**  
They treat rules as causal statements.

**Reality:**  
Rules are correlation-based.

**Risk:**  
Wrong business decisions.

---

## Q4. Why does pruning matter more than split criterion?

**Why:**  
Overfitting is controlled by tree size, not impurity formula.

**Insight:**  
Depth regularization beats Gini vs Entropy debates.

---

## Q5. How is pruning actually used in practice?

**Methods:**  
- max_depth
- min_samples_leaf
- cost-complexity pruning

**Approach:**  
Tune via cross-validation.

---

## Q6. Why do trees struggle with noisy, high-dimensional data?

**Why:**  
Greedy splits exploit random noise.

**Effect:**  
Spurious patterns get locked in.

---

## Q7. How do trees behave under data drift?

**Why:**  
Partition boundaries become misaligned.

**Effect:**  
Sudden performance drops.

---

## Q8. Why are trees sensitive to class imbalance?

**Why:**  
Impurity measures favor majority class splits.

**Fixes:**  
- Class weights
- Balanced subsampling

---

## Q9. How do trees handle missing values in practice?

**Reality:**  
Most libraries require preprocessing.

**Solutions:**  
- Imputation
- Surrogate splits (if available)

---

## Q10. Why is tree retraining expensive operationally?

**Why:**  
Structure changes require re-validation and explanation.

**Impact:**  
Harder governance.

---

## Q11. When is a single Decision Tree actually a good choice?

**Cases:**  
- Very small datasets
- Strong interpretability requirements
- Educational or rule-discovery tasks

---

## Q12. Why do teams move quickly from trees to ensembles?

**Why:**  
Ensembles reduce variance.

**Core idea:**  
Averaging stabilizes predictions.

---

## Q13. How does a tree compare to linear models in production?

**Trees:**  
- Flexible
- High variance

**Linear models:**  
- Stable
- Easier to monitor

---

## Q14. Why are trees rarely used alone in regulated industries?

**Why:**  
Instability complicates audits.

**Preference:**  
Simpler, more stable models.

---

## Q15. How do experienced teams use Decision Trees?

**Practically:**  
- As baselines
- For feature interaction discovery
- Inside ensembles

---

## Q16. Biggest real-world mistake with Decision Trees?

**Answer:**  
Deploying an unpruned tree.

---

## Q17. Real-world takeaway

Decision Trees are powerful **exploratory tools**, but fragile **production models**.

Their weaknesses directly explain why Random Forests and Boosting exist.

---

📌 **Decision Trees complete. Next: Random Forests — turning instability into strength.**

