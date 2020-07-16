from sklearn import random_projection
import pandas as pd
from sklearn.preprocessing import StandardScaler
import preprocessing

def perform_randomProj():
    X_train, y_train, X_test, y_test = preprocessing.data_loader()
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(X_train)
    X_train = pd.DataFrame(x_train_scaled, index=X_train.index, columns=X_train.columns)
    X_test = pd.DataFrame(scaler.fit_transform(X_test), index=X_test.index, columns=X_test.columns)
    transformer = random_projection.GaussianRandomProjection(n_components=34)
    transformer.fit(X_train)
    columns = ['randomProj_%i' % i for i in range(transformer.components_.shape[0])]
    X_train = pd.DataFrame(transformer.transform(X_train), columns=columns, index=X_train.index)
    X_test = pd.DataFrame(transformer.transform(X_test), columns=columns, index=X_test.index)
    return X_train, X_test, y_train, y_test


perform_randomProj()