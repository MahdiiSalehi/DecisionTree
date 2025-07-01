#In the name of ALLAH!
#Mahdi Salehi

from linked_list import LinkedList as LL

class Node:
    "Node for Map."
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = self

class Map:
    "Map key value."
    def __init__(self) -> None:
        self.last = None
        self.size = 0
    
    def __getitem__(self, key):
        cur = self.last
        for i in range(self.size):
            if cur.key == key:
                return cur.val
            cur = cur.next
        raise KeyError
    
    def __setitem__(self, key, val):
        cur = self.last
        for i in range(self.size):
            if cur.key == key:
                cur.val = val
                return
            cur = cur.next
        raise KeyError
    
    def __contains__(self, key):
        cur = self.last
        for i in range(self.size):
            if cur.key == key:
                return True
            cur = cur.next
        return False
    
    def __str__(self):
        if not self.size:
            return ""
        cur = self.last.next
        temp = '{'+ str(cur.key) + ':' + str(cur.val)
        for i in range(self.size - 1):
            cur = cur.next
            temp += ', ' + str(cur.key) + ':' + str(cur.val)
        temp += '}'
        return temp
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return Iterator(self)
    
    def values(self):
        ls = LL()
        cur = self.last
        if self.size:
            cur = cur.next
        for i in range(self.size):
            ls.insert(cur.val)
            cur = cur.next
        return ls
    
    def keys(self):
        ls = LL()
        cur = self.last.next
        for i in range(self.size):
            ls.insert(cur.key)
            cur = cur.next
        return ls
    
    def insert(self, key, val, index=-1):
        if (index < -1) or (index > self.size):
            raise IndexError
        new_node = Node(key, val)
        if not self.last:
            self.last = new_node
            self.size += 1
            return
        if index == -1 or index == self.size:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node
            self.size += 1
            return
        if not index:
            new_node.next = self.last.next
            self.last.next = new_node
            self.size += 1
            return
        cur = self.last
        for i in range(index):
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1

    def remove(self, index=-1):
        if (index < -1) or (index >= self.size):
            raise IndexError
        if index == -1:
            index = self.size - 1
        cur = self.last
        for i in range(index):
            cur = cur.next
        node = cur.next
        cur.next = cur.next.next
        if index == -1 or index == self.size - 1:
            self.last = cur
        self.size -= 1
        if not self.size:
            self.last = None
    
class Iterator:
    """Iterator for Map."""
    def __init__(self, map) -> None:
        self.len = map.size
        self.cur = map.last
        if self.len:
            self.cur = self.cur.next
    
    def __next__(self):
        if self.len:
            self.len -= 1
            ls = LL()
            ls.insert(self.cur.key)
            ls.insert(self.cur.val)
            self.cur = self.cur.next
            return ls
        else:
            raise StopIteration