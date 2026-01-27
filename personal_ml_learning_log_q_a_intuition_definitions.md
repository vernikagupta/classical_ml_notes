# Personal Machine Learning Notes

This document is a **living record** of your learning journey. It is designed so that you can:
- Revisit *exact questions you asked*
- Recall *why each concept exists*
- Read *plain‑English intuition*
- See *formal definitions only after meaning is clear*

Think of this as **your personal ML notebook**, not a textbook.

---

## HOW TO USE THIS DOCUMENT

For every concept, you will see four parts:
1. **Question (in natural language)** – like you would ask in an interview or while studying
2. **Intuition (story / mental model)** – what the model is really doing
3. **Formal meaning** – precise but readable definition
4. **Key sentence to remember** – one line that locks the concept

You can keep adding to this document over time.

---

# SECTION 1: LINEAR REGRESSION

## Q1. What is Linear Regression really doing?

### Intuition
Linear regression tries to draw the *best straight relationship* between inputs and output so that prediction errors are minimized overall.

### Formal meaning
Linear regression models the dependent variable as a linear combination of independent variables and minimizes Mean Squared Error.

### Key sentence
Linear regression finds the best-fitting linear relationship between features and a continuous target.

---

## Q2. Why do we use Mean Squared Error?

### Intuition
We want large mistakes to hurt more than small ones, and we want a smooth function that optimization algorithms can work with.

### Formal meaning
MSE is the average of squared differences between actual and predicted values and corresponds to Gaussian noise assumptions.

### Key sentence
MSE penalizes large errors more heavily and is mathematically convenient for optimization.

---

# SECTION 2: LOGISTIC REGRESSION

## Q3. Why is logistic regression called regression?

### Intuition
Because we still compute a linear combination of features; we just pass it through a function to convert it into probability.

### Formal meaning
Logistic regression models the log‑odds of the target as a linear function of input features.

### Key sentence
Logistic regression is a linear model applied to log‑odds, not directly to the class label.

---

## Q4. Why do we use sigmoid?

### Intuition
We want any real number to behave like a probability—between 0 and 1—without hard cutoffs.

### Formal meaning
The sigmoid function maps real‑valued logits to probabilities and is differentiable everywhere.

### Key sentence
Sigmoid converts linear outputs into interpretable probabilities.

---

## Q5. Why log loss and not MSE?

### Intuition
Wrong and confident predictions should be punished much more than uncertain ones.

### Formal meaning
Log loss is derived from Bernoulli maximum likelihood and penalizes confident wrong predictions exponentially.

### Key sentence
Log loss aligns probabilistic predictions with true labels and discourages overconfidence.

---

# SECTION 3: PROBABILITY & BAYES

## Q6. Probability vs Likelihood

### Intuition
Probability asks: what might happen?
Likelihood asks: what parameters explain what already happened?

### Formal meaning
Probability treats parameters as fixed and outcomes as random, while likelihood treats data as fixed and parameters as variables.

### Key sentence
Likelihood reverses the direction of reasoning compared to probability.

---

## Q7. What does Bayes’ theorem actually do?

### Intuition
It updates what you believed earlier using new evidence.

### Formal meaning
Bayes’ theorem computes posterior probability by combining prior belief and likelihood of observed data.

### Key sentence
Bayes’ theorem is a belief‑updating rule.

---

# SECTION 4: NAIVE BAYES CLASSIFIER

## Q8. How does Naive Bayes classify a point?

### Intuition
It assumes each class in turn and asks which class best explains the data.

### Formal meaning
Naive Bayes predicts the class that maximizes P(x|y)·P(y) under a conditional independence assumption.

### Key sentence
Naive Bayes chooses the class that most likely generated the data.

---

## Q9. Why is it called “naive”?

### Intuition
Because it pretends features don’t affect each other once the class is known.

### Formal meaning
It assumes conditional independence among features given the class.

### Key sentence
The naivety is the independence assumption, not the algorithm itself.

---

## Q10. Why is Laplace smoothing needed?

### Intuition
One unseen feature should not make a class impossible.

### Formal meaning
Laplace smoothing prevents zero probabilities by adding a small constant to feature counts.

### Key sentence
Laplace smoothing avoids zero‑probability failures.

---

# SECTION 5: DECISION TREES

## Q11. What is a good split?

### Intuition
A good question is one that separates the data cleanly.

### Formal meaning
A good split maximizes impurity reduction (Information Gain or Gini reduction).

### Key sentence
Decision trees greedily choose splits that increase purity.

---

## Q12. What does Gini impurity really mean?

### Intuition
It measures how mixed a node is—how often a random guess would be wrong.

### Formal meaning
Gini impurity equals the expected probability of misclassification based on class proportions.

### Key sentence
Higher Gini means higher chance of misclassification.

---

## Q13. Why is Gini zero for a pure node?

### Intuition
If all samples belong to one class, you can never guess wrong.

### Formal meaning
When one class probability is 1, the sum of squared probabilities is 1, making Gini zero.

### Key sentence
Pure nodes have zero impurity.

---

# SECTION 6: METRICS & PRACTICAL ML

## Q14. Why is accuracy bad for imbalanced data?

### Intuition
Predicting the majority class always can still look good.

### Formal meaning
Accuracy ignores class distribution and error type costs.

### Key sentence
Accuracy hides failure on minority classes.

---

## Q15. Precision vs Recall

### Intuition
Precision asks: am I correct when I say yes?
Recall asks: did I miss any yes?

### Formal meaning
Precision = TP/(TP+FP), Recall = TP/(TP+FN).

### Key sentence
Precision controls false alarms, recall controls misses.

---

# END NOTE

This document is meant to **grow with you**.

Anytime you want:
- New questions added
- Your own wording preserved
- Examples rewritten

Just say: **“Add this to my learning log.”**

---

**End of Personal ML Learning Log**

