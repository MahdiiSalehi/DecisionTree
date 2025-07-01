#In the name of ALLAH!
#Mahdi Salehi

from random import randint
from linked_list import LinkedList as LL
from my_array import Array
from decision_tree_classifier import DTreeClassifier as DTC
from map import Map
from settings import *
#from main import train_features, train_labels, train_rows, test_labels

class RFClassifier:
    """Random forest classifier."""
    def __init__(self) -> None:
        self.DCtrees = Array(NUM_OF_ESIMATOR)
        features_indexes = Array(col)
        rows_indexes = Array(row)
        total = row
        for i in range(NUM_OF_ESIMATOR):
            start = randint(0, int(total/2))
            end = randint(int(total/2) + 1, total - 1)
            self.DCtrees[i] = DTC(features_indexes, rows_indexes[start:end+1])
    
    def predict(self, row : LL, depth : int):
        predicted_labels = Array(NUM_OF_ESIMATOR)
        for i in range(NUM_OF_ESIMATOR):
            predicted_labels[i] = self.DCtrees[i].predict(row, depth)
        map = Map()
        for label in predicted_labels:
            if label in map:
                map[label] += 1
            else:
                map.insert(label, 1)
        max_value = best_key = 0
        for key, val in map:
            if val > max_value:
                max_value = val
                best_key = key
        return best_key
    
    def predict_all(self, in_rows : Array, depth : int):
        predicted_labels = Array(len(in_rows))
        for i in range(len(in_rows)):
            predicted_labels[i] = Array(NUM_OF_ESIMATOR)
        for i in range(len(self.DCtrees)):
            temp = self.DCtrees[i].predict_all(in_rows, depth)
            for j in range(len(in_rows)):
                predicted_labels[j][i] = temp[j]
        best_keys = Array(len(in_rows))
        for i in range(len(predicted_labels)):
            map = Map()
            for label in predicted_labels[i]:
                if label in map:
                    map[label] += 1
                else:
                    map.insert(label, 1)
            max_value = best_key = 0
            for key, val in map:
                if val > max_value:
                    max_value = val
                    best_key = key
            best_keys[i] = best_key
        return best_keys
    
    def accuracy(self, predicted_labels : Array):
        total = len(test_labels)
        similarity = 0
        for i in range(total):
            if test_labels [i] == predicted_labels[i]:
                similarity += 1
        return similarity * 100 / total

    def print(self):
        for DCtree in self.DCtrees:
            DCtree.print()