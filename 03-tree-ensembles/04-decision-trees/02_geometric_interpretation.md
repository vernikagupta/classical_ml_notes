# Decision Trees — Geometric Interpretation (How Trees Partition Space)

This chapter explains **what Decision Trees do geometrically**. Understanding this removes confusion about why trees look “blocky”, why they overfit, and why ensembles help so much.

> If linear models draw lines and planes, trees carve space into rectangles.

---

## Q1. What geometry does a Decision Tree impose on feature space?

**What:**  
Decision Trees partition feature space into **axis-aligned regions**.

**Why axis-aligned:**  
Each split tests a single feature at a time (x_j ≤ t).

**Consequence:**  
All decision boundaries are parallel to coordinate axes.

---

## Q2. How does a single split look geometrically?

**What:**  
A single split creates a **half-space cut**.

**Example (2D):**  
- x₁ ≤ t → left region
- x₁ > t → right region

This is a **vertical or horizontal line**, never diagonal.

---

## Q3. How do multiple splits combine geometrically?

**What:**  
Multiple splits create **rectangular (hyper-rectangular) regions**.

**Intuition:**  
Each split further subdivides an existing region.

**Result:**  
A grid-like partition of space.

---

## Q4. What does a leaf node represent geometrically?

**What:**  
A leaf corresponds to a **region in feature space**.

**Prediction meaning:**  
The model predicts a constant value for all points in that region.

---

## Q5. Why are Decision Tree predictions piecewise constant?

**Why:**  
Within a leaf, no further splits exist.

**Consequence:**  
The prediction jumps at region boundaries.

---

## Q6. How does tree depth affect geometry?

**Shallow tree:**  
- Few large rectangles
- High bias

**Deep tree:**  
- Many small rectangles
- Low bias, high variance

---

## Q7. Why do trees approximate smooth functions poorly?

**Why:**  
Smooth functions require curved boundaries.

**Tree limitation:**  
Axis-aligned rectangles approximate curves using many small steps.

---

## Q8. How do trees capture non-linear relationships?

**How:**  
By stacking many splits.

**Interpretation:**  
Non-linearity emerges from piecewise linear partitions.

---

## Q9. Why do trees naturally model interactions?

**Why:**  
Splits at deeper levels are conditional on earlier splits.

**Geometry:**  
Regions depend on combinations of feature thresholds.

---

## Q10. Why are trees insensitive to feature scaling?

**Why:**  
Splits depend only on ordering, not magnitude.

**Geometry:**  
Rescaling stretches axes but preserves order.

---

## Q11. Why are trees sensitive to feature rotation?

**Why:**  
Trees cannot create diagonal splits.

**Effect:**  
A rotated feature space may require many more splits.

---

## Q12. What does overfitting look like geometrically?

**What:**  
Tiny rectangles tightly wrapping training points.

**Visual intuition:**  
A checkerboard of micro-regions.

---

## Q13. How does pruning change geometry?

**What:**  
Pruning merges adjacent regions.

**Effect:**  
Simpler, larger rectangles.

---

## Q14. How does regularization appear geometrically in trees?

**Tree regularization:**  
- max_depth
- min_samples_leaf
- min_impurity_decrease

**Geometry effect:**  
Limits how small rectangles can get.

---

## Q15. Why do trees extrapolate poorly?

**Why:**  
Outside training range, trees predict constant leaf values.

**Contrast:**  
Linear models extrapolate linearly; trees do not.

---

## Q16. How does geometry explain tree instability?

**Why:**  
Small data changes → different early splits.

**Effect:**  
Entire partition structure changes.

---

## Q17. How do ensembles fix geometric weaknesses?

**Random Forests:**  
Average many different partitions.

**Boosting:**  
Sequentially refines partitions.

**Result:**  
Smoother effective decision boundaries.

---

## Q18. Visual references (strongly recommended)

- Axis-aligned partitions visualization:
https://scikit-learn.org/stable/auto_examples/tree/plot_iris_decision_boundaries.html

- Why trees are blocky:
https://towardsdatascience.com/why-decision-trees-are-not-rotation-invariant-43c3d27f7e5d

---

## Q19. Geometric takeaway

Decision Trees:
- Partition space with rectangles
- Approximate functions piecewise
- Overfit by creating tiny regions

This geometry explains **everything** about tree behavior.

---

📌 **Next:** Tricky interview questions on Decision Trees — common traps and deep reasoning.