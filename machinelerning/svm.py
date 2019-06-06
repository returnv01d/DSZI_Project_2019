import warnings

from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

class SVM:

    @staticmethod
    def svm(example):
        X = SVM.read_features_from_file('learnDataFeatures.txt')
        y = SVM.read_labels_from_file('learnDataLabels.txt')

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
        clf = svm.SVC(gamma='scale')
        clf.fit(X_train, y_train)
        print ('Support Vector Machines method - Waiter move:', clf.predict([example]))

        svclassifier = SVC(kernel='linear')
        svclassifier.fit(X_train, y_train)
        y_pred = svclassifier.predict(X_test)

        warnings.filterwarnings('ignore')
        print('Raport SVM: ', classification_report(y_test, y_pred))





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

