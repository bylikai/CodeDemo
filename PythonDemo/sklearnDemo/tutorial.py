
from sklearn import datasets
from sklearn import svm
from sklearn import linear_model

iris = datasets.load_iris()
digits = datasets.load_digits()
digits.images[0]

clf = svm.SVC( gamma=0.001, C=100.)

#print( iris )
print( digits.data )

'''
linear_model test...
'''
reg = linear_model.LinearRegression()
reg.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

'''
Ridge Regression
'''
reg = linear_model.Ridge (alpha = .5)
reg.fit ([[0, 0], [0, 0], [1, 1]], [0, .1, 1]) 
reg.coef_

