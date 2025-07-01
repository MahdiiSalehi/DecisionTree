#In the name of ALLAH!
#Mahdi Salehi

from math import log2 as log
from binarytree import build
from my_array import Array
from linked_list import LinkedList as LL
from map import Map
from settings import *
#from main import train_features, train_labels, train_rows, test_labels

class best_feature:
    def __init__(self) -> None:
        self.sep = None
        self.index_feature = None
        self.len_l_rows = None
        self.len_r_rows = None
        self.r_entrp = None
        self.l_entrp = None

    def set(self, sep, index_feature, l_entrp, r_entrp, len_l_rows, len_r_rows):
        self.sep = sep
        self.index_feature = index_feature
        self.len_l_rows = len_l_rows
        self.len_r_rows = len_r_rows
        self.l_entrp = l_entrp
        self.r_entrp = r_entrp


class TNode:
    "Tree Node."
    def __init__(self, val=None, index_feature=None, label=None) -> None:
        self.val = val
        self.index_feature = index_feature
        self.label = label
        self.right = None
        self.left = None

class TLNode:
    "Tree leaf Node."
    def __init__(self, label=None) -> None:
        self.label = label

class Tree:
    "Tree for create Decisiion Tree."
    def __init__(self, features_indexes, rows_indexes) -> None:
        self.depth = 0
        self.root = self._create_node(10, features_indexes, rows_indexes, self.depth + 1)

    def _create_node(self, p_entrp : float, features_indexes : Array, rows_indexes : Array, depth):

        if depth > self.depth:
            self.depth = depth

        best = best_feature()
        max_gain = -100000

        for i in features_indexes:
            feature = train_features[i]
            values = LL()
            for j in rows_indexes:
                val = feature[j]
                if val not in values:
                    k = 0
                    while (k < len(values) and values[k] < val):
                        k += 1
                    values.insert(val, k)
            if len(values) <= 1:
                continue
            for val in values:
                left = Map()
                right = Map()
                for j in rows_indexes:
                    data = feature[j]
                    label = train_labels[j]
                    if data < val:
                        if label not in left:
                            left.insert(label, 1)
                        else:
                            left[label] += 1
                    else:
                        if label not in right:
                            right.insert(label, 1)
                        else:
                            right[label] += 1
                
                l_entrp = self._entropy(left)
                r_entrp = self._entropy(right)

                num_l = 0
                for valu in left.values():
                    num_l += valu
                num_r = 0
                for valu in right.values():
                    num_r += valu
                total = num_l + num_r
                w_l = float(num_l) / total
                w_r = float(num_r) / total
                
                gain = self._i_gain(p_entrp, l_entrp, r_entrp, w_l, w_r)

                if gain > max_gain:
                    best.set(val, i, l_entrp, r_entrp, num_l, num_r)
                    max_gain = gain
        
        if best.sep == None:
            map = Map()
            for i in rows_indexes:
                key = train_labels[i]
                if key not in map:
                    map.insert(key, 1)
                else:
                    map[key] += 1
            best_key = max_val = 0
            for key, val in map:
                if val > max_val:
                    best_key = key
                    max_val = val
            return TLNode(best_key)
        
        new_node = TNode()
        new_node.val = best.sep
        new_node.index_feature = best.index_feature

        map = Map()
        for i in rows_indexes:
            key = train_labels[i]
            if key not in map:
                map.insert(key, 1)
            else:
                map[key] += 1
        best_key = max_val = 0
        for key, val in map:
            if val > max_val:
                best_key = key
                max_val = val
        new_node.label = best_key

        child_features = Array(len(features_indexes) - 1)
        j = 0
        for i in features_indexes:
            if i != best.index_feature:
                child_features[j] = i
                j += 1
        
        l_rows = Array(best.len_l_rows)
        feature = train_features[best.index_feature]
        j = 0
        for i in rows_indexes:
            if feature[i] < best.sep:
                l_rows[j] = i
                j += 1
        
        if p_entrp <= best.l_entrp:
            map = Map()
            for i in l_rows:
                key = train_labels[i]
                if key not in map:
                    map.insert(key, 1)
                else:
                    map[key] += 1
            best_key = max_val = 0
            for key, val in map:
                if val > max_val:
                    best_key = key
                    max_val = val
            new_node.left = TLNode(best_key)
        else:
            same_labels = True
            temp = train_labels[l_rows[0]]
            for i in l_rows:
                if temp != train_labels[i]:
                    same_labels = False
                    break
            if same_labels:
                new_node.left = TLNode(temp)
            else:
                new_node.left = self._create_node(best.l_entrp, child_features, l_rows, depth + 1)
        
        r_rows = Array(best.len_r_rows)
        feature = train_features[best.index_feature]
        j = 0
        for i in rows_indexes:
            if feature[i] >= best.sep:
                r_rows[j] = i
                j += 1
        
        if p_entrp <= best.r_entrp:
            map = Map()
            for i in r_rows:
                key = train_labels[i]
                if key not in map:
                    map.insert(key, 1)
                else:
                    map[key] += 1
            best_key = max_val = 0
            for key, val in map:
                if val > max_val:
                    best_key = key
                    max_val = val
            new_node.right = TLNode(best_key)
        else:
            same_labels = True
            temp = train_labels[r_rows[0]]
            for i in r_rows:
                if temp != train_labels[i]:
                    same_labels = False
                    break
            if same_labels:
                new_node.right = TLNode(temp)
            else:
                new_node.right = self._create_node(best.r_entrp, child_features, r_rows, depth + 1)
        
        return new_node

    def _entropy(self, values:Map):
        total = 0
        entrp = 0
        for val in values.values():
            total += val
        for val in values.values():
            prob = float(val)/total
            entrp -= prob * log(prob)
        return entrp
    
    def _i_gain(self, p_entrp, l_entrp, r_entrp, w_l, w_r):
        return p_entrp - l_entrp * w_l - r_entrp * w_r
    
    def get_depth(self):
        return self.depth
    
    def print(self) -> str:
        if not self.root:
            return ""
        nodes = LL()
        nodes.insert(self.root)
        is_valid = True
        i = 0
        while(is_valid):
            p = nodes[i]
            if type(p) == TNode:
                nodes.insert(p.left)
                nodes.insert(p.right)
            else:
                nodes.insert(None)
                nodes.insert(None)
            is_valid = False
            for j in range(i + 1, len(nodes)):
                if nodes[j] != None:
                    is_valid = True
                    break
            i += 1
        i = len(nodes) - 1
        while(nodes[i] == None):
            nodes.pop(i)
            i -= 1
        for i in range(len(nodes)):
            try:
                nodes[i] = names[nodes[i].index_feature]
            except:
                try:
                    nodes[i] = nodes[i].label
                except:
                    pass
        file = open(DRAW_FILE_PATH, "a")
        print(build(nodes), file=file, flush=True)
        print('\n', file=file, flush=True)
