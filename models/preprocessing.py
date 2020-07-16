import pandas as pd
import random


def data_loader(filename='train_V2.csv', test_size=.10):
    

    data = pd.read_csv(filename)
    train_size = 1-test_size
    #Remove attributes that are presumed to be irrelevant [Id, groupId]
    data.drop(['Id', 'groupId'], axis=1, inplace=True)

    #one hot_encode match type
    data_dummies = pd.get_dummies(data['matchType'], prefix='matchType')
    data = pd.concat([data, data_dummies], axis=1)
    data.drop(['matchType'], axis=1, inplace=True)
    # print(data.isna().any())
    print("before drop NaNs")
    print(data.shape)
    data = data.dropna()
    print("after drop NaNs")
    print(data.shape)
    #Split into training and testing sets
    #split based on matchID
    #want all data from a given match to be together (in test or train)
    #Don't want dependent data in train and test
    matches = data.matchId.unique().tolist()
    num_training = int(len(matches)*train_size)
    train_matches = random.sample(matches, num_training)
    train_data = data[data.matchId.isin(train_matches)]
    test_data = data[~data.matchId.isin(train_matches)]

    #No need for matcId anymore
    train_data.drop(['matchId'], axis=1, inplace=True)
    test_data.drop(['matchId'], axis=1, inplace=True)



    y_train = train_data['winPlacePerc']
    x_train = train_data.drop('winPlacePerc', axis=1)

    y_test = test_data['winPlacePerc']
    x_test = test_data.drop('winPlacePerc', axis=1)




    return x_train, y_train, x_test, y_test

#x_train, y_train, x_test, y_test = data_loader()
