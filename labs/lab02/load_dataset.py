# Lab 02: load the UCI "Predict Students' Dropout and Academic Success" dataset
# Install first:  pip install ucimlrepo

from ucimlrepo import fetch_ucirepo

# fetch dataset (id=697)
predict_students_dropout_and_academic_success = fetch_ucirepo(id=697)

# data (as pandas dataframes)
X = predict_students_dropout_and_academic_success.data.features
y = predict_students_dropout_and_academic_success.data.targets

# metadata
print(predict_students_dropout_and_academic_success.metadata)

# variable information
print(predict_students_dropout_and_academic_success.variables)

# quick sanity check
print("Features shape:", X.shape)
print("Targets shape:", y.shape)