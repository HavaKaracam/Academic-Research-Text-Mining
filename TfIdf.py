import math


class TfIdf:

    @staticmethod
    def computeIdf(word, files):
        counter = 0
        for file in files:
            if word in file:
                counter += 1
                continue
        idf = math.log10(len(files)/counter)
        return idf

    def computeTfIdf(idf, termFreq):
        tf_idf = termFreq * idf
        return tf_idf