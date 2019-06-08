class ReadFromFile:

    @staticmethod
    def read_features_from_file(filepath):
        file = open(filepath, 'r')
        listOfFeatures = []
        for line in file:
            newLine = []
            for i in line:
                if i != '\n':
                    newLine.append(i)
            listOfFeatures.append(newLine)

        return listOfFeatures


    @staticmethod
    def read_labels_from_file(filepath):
        file = open(filepath, 'r')
        listOfLabels = file.read().split()
        return listOfLabels