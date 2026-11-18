# Lab 02 Report: Classical Machine Learning Pipeline

## Table 2.1: Tuning results
(paste the tuning table from Task 4)

## Task 6: Interpretation
1. Which model would you trust for an early-warning system?
I would trust the tuned random forest (max_depth = 20) for an early-warning system, because it had the best validation macro F1 (0.726) and scored higher than logistic regression in 5-fold cross-validation (0.720 vs 0.702). On the test set it caught 70.4% of Dropout students with 0.820 precision, which makes it the more dependable option for flagging at-risk students.

2. Which class does it struggle with?
3. One deployment risk.

