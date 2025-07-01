#In the name of ALLAH!
#Mahdi Salehi

from tree import Tree , TLNode
from my_array import Array
from linked_list import LinkedList as LL
#from main import train_features, train_labels, train_rows, test_labels

class DTreeClassifier:
    """Decision tree classifier."""
    def __init__(self, features_indexes, rows_indexes) -> None:
        self.tree = Tree(features_indexes, rows_indexes)

    def predict(self, row : Array, depth : int):
        p = self.tree.root
        while depth > 0 and type(p) != TLNode:
            if row[p.index_feature] < p.val:
                p = p.left
            else:
                p = p.right
            depth -= 1
        return p.label
    
    def  predict_all(self, rows : Array, depth):
        out = Array(len(rows))
        for i in range(len(rows)):
            row = rows[i]
            temp = depth
            p = self.tree.root
            while temp > 0 and type(p) != TLNode:
                if row[p.index_feature] < p.val:
                    p = p.left
                else:
                    p = p.right
                temp -= 1
            out[i] = p.label
        return out

    def accuracy(self, labels : Array, predicted_labels : Array):
        total = len(labels)
        similarity = 0
        for i in range(total):
            if labels [i] == predicted_labels[i]:
                similarity += 1
        return similarity * 100 / total
    
    def print(self) -> str:
        self.tree.print()
    