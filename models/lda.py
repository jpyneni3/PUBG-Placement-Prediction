from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import pandas as pd
from sklearn.preprocessing import StandardScaler
import preprocessing

def perform_lda():
    X_train, y_train, X_test, y_test = preprocessing.data_loader()
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(X_train)
    X_train = pd.DataFrame(x_train_scaled, index=X_train.index, columns=X_train.columns)
    X_test = pd.DataFrame(scaler.fit_transform(X_test), index=X_test.index, columns=X_test.columns)
    lda = LinearDiscriminantAnalysis()
    lda.fit(X_train, y_train)
    columns = ['lda_%i' % i for i in range(lda.explained_variance_ratio_.shape[0])]
    X_train = pd.DataFrame(lda.transform(X_train), columns=columns, index=X_train.index)
    X_test = pd.DataFrame(lda.transform(X_test), columns=columns, index=X_test.index)
    print(X_train.head())
    print(X_test.head())
    return X_train, X_test, y_train, y_test


perform_lda()