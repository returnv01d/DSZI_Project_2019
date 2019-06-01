import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree

class DecisionTree:

    @staticmethod
    def decisionTree():
        # Importing Dataset

        dataset = pd.read_csv('patientData.csv')
        X = dataset.iloc[:, :-1].values
        Y = dataset.iloc[:, 1].values

        # Handing Missing Dataset

        # from sklearn.preprocessing import Imputer
        # imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
        # imputer = imputer.fit(X[:, 1:3])
        # X[:, 1:3] = imputer.transform(X[:, 1:3])

        # Encode Categorical Data

        from sklearn.preprocessing import LabelEncoder, OneHotEncoder
        labelencoder_X = LabelEncoder()
        X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
        onehotencoder = OneHotEncoder(categorical_features=[0])
        X = onehotencoder.fit_transform(X).toarray()
        labelencoder_Y = LabelEncoder()
        Y = [1, 2, 3, 4]

        # Split the data between the Training Data and Test Data

        from sklearn.model_selection import train_test_split
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2
                                                            , random_state=0)

        # Feature Scaling

        from sklearn.preprocessing import StandardScaler
        sc_X = StandardScaler()
        X_train = sc_X.fit_transform(X_train)
        X_test = sc_X.transform(X_test)

        clf = tree.DecisionTreeRegressor()

        clf = clf.fit(X, Y)
        print(clf.predict([[0, 0]]))