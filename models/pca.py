import pandas as pd 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import preprocessing

def perform_pca():
    X_train, y_train, X_test, y_test = preprocessing.data_loader()
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(X_train)
    X_train = pd.DataFrame(x_train_scaled, index=X_train.index, columns=X_train.columns)
    X_test = pd.DataFrame(scaler.fit_transform(X_test), index=X_test.index, columns=X_test.columns)
    pca = PCA(0.99)
    pca.fit(X_train)
    print(pca.components_.shape)
    columns = ['pca_%i' % i for i in range(pca.components_.shape[0])]
    X_train = pd.DataFrame(pca.transform(X_train), columns=columns, index=X_train.index)
    X_test = pd.DataFrame(pca.transform(X_test), columns=columns, index=X_test.index)
    return X_train, X_test, y_train, y_test

perform_pca()