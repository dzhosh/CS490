from sklearn import svm
from sklearn import naive_bayes
from sklearn.model_selection import train_test_split
import pandas as pd

# Read File and Separate Training and Test Sets
iris = pd.read_csv('iris.csv')
x = iris[['sepal length', 'sepal width', 'petal length', 'petal width']]
y = iris['class']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# 1
# Implement Naive Bayes method using scikit-learn library
# Use cross validation to create training and testing part
# Evaluate the model on testing part

model_1 = naive_bayes.GaussianNB()
model_1.fit(x_train, y_train)
print('Accuracy of Naive Bayes Model: {:.2f}'.format(model_1.score(x_test, y_test)))

# 2
# Implement linear SVM method using scikit library
# Use the same data set above
# Which algorithm you got better accuracy? Can you justify why?

model_2 = svm.SVC(kernel='linear', C=1)
model_2.fit(x_train, y_train)
print('Accuracy of Linear Support Vector Machines Model: {:.2f}'.format(model_2.score(x_test, y_test)))

# The Linear SVM model provides a slightly more accurate result
# This is likely due to a strong linear separation of the different iris classes.

# 3
# Use the SVM with RBF kernel on the same data set.
# How the result changed?

model_3 = svm.SVC(kernel='rbf', gamma='scale')
model_3.fit(x_train, y_train)
print('Accuracy of RBF Support Vector Machines Model: {:.2f}'.format(model_3.score(x_test, y_test)))

# The accuracy of the rbf kernel is relatively the same as the linear kernel.
# Both usually give upper 90% in test accuracy.
