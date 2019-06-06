from sklearn import tree

from machinelerning.readFromFile import ReadFromFile


class DecisionTree:

    @staticmethod
    def decisiontree(example):
        features = ReadFromFile.read_features_from_file('learnDataFeatures.txt')
        labels = ReadFromFile.read_labels_from_file('learnDataLabels.txt')
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(features, labels)
        return clf.predict([example])
        #print('Decision Tree method - Waiter move: ', clf.predict([example]))
