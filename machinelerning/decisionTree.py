from sklearn import tree

from machinelerning.readFromFile import ReadFromFile


class DecisionTree:

    @staticmethod
    def decisiontree(example):
        # 0-FreeSpace, 1-Carpet, 2-Kitchen, 3-Table, 5-Waiter

        features = ReadFromFile.read_features_from_file('learnDataFeatures.txt')
        labels = ReadFromFile.read_labels_from_file('learnDataLabels.txt')
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(features, labels)
        print('Decision Tree method - Waiter move: ', clf.predict([example]))
