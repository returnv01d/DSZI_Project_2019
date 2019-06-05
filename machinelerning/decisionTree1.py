from sklearn import tree

class DecisionTree1:

    @staticmethod
    def decisiontree1():
        features = [[40, 1], [40, 1], [50, 0], [50, 0]]
        labels = [0, 0, 1, 1]
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(features, labels)
        print(clf.predict([[40, 1]]))

