class ReadFromFile:

    @staticmethod
    def read_features_from_file(filepath):
        file = open(filepath, 'r')
        listOfFeatures = []
        for i in range(0, 47):
            line = file.readline().split(';')
            newline = list(map(int, line[0].split(',')))
            listOfFeatures.append(newline)
        return listOfFeatures


    @staticmethod
    def read_labels_from_file(filepath):
        file = open(filepath, 'r')
        listOfLabels = file.read().split()
        return listOfLabels