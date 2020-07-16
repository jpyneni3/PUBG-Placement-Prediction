import pandas as pd
import preprocessing


def validation(x_train, y_train):
    data = pd.concat([x_train, y_train], axis=1)
    val = data.sample(frac=0.1)
    data = pd.concat([data, val, val]).drop_duplicates(keep=False)
    y_train = data['winPlacePerc']
    x_train = data.drop('winPlacePerc', axis=1)
    y_val = val['winPlacePerc']
    x_val = val.drop('winPlacePerc', axis=1)
    return x_train, y_train, x_val, y_val

