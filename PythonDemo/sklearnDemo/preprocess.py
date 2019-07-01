from sklearn import preprocessing
import numpy as np
X_train = np.array([[ 1., -1.,  2.],
                    [ 2.,  0.,  0.],
                    [ 0.,  1., -1.]])
 
X_test = np.array([[ -3., -1.,  4.]])


def min_max_process( X ):
    min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
    X_train_minmax = min_max_scaler.fit_transform(X)

    print(X_train_minmax)

    X_train_minmax = min_max_scaler.fit_transform(X.T)
    print(X_train_minmax)

min_max_process( X_train )
min_max_process( X_test )

X_scaled = preprocessing.scale(X_train)
print(X_scaled)