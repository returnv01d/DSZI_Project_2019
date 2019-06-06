from sklearn import tree

class DecisionTree1:

    @staticmethod
    def decisiontree1(example):
        # 0-FreeSpace, 1-Carpet, 2-Kitchen, 3-Table, 5-Waiter

        features = DecisionTree1.read_features_from_file('learnDataFeatures.txt')
        labels = DecisionTree1.read_labels_from_file('learnDataLabels.txt')
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(features, labels)
        print('Decision Tree method - Waiter move: ', clf.predict([example]))


    @staticmethod
    def read_features_from_file(filepath):
        file = open(filepath, 'r')
        listOfFeatures = []
        for i in range(0, 24):
            line = file.readline().split(';')
            newline = list(map(int, line[0].split(',')))
            listOfFeatures.append(newline)
        return listOfFeatures


    @staticmethod
    def read_labels_from_file(filepath):
        file = open(filepath, 'r')
        listOfLabels = file.read().split()
        return listOfLabels


