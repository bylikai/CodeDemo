from sklearn import linear_model
import matplotlib.pyplot as plt


X=[ [0.,0.], [1.,1.], [2.,2.], [3., 3.] ]
Y=[ 0., 1., 2., 3. ]

reg = linear_model.BayesianRidge()

reg.fit( X, Y )

reg.predict( [[1, 0.]] )

reg.coef_

plt.plot( reg.coef_, color='lightgreen', linewidth = 2, label='Bayesian Ridge estimate' )

plt.show()