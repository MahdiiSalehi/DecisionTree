#In the name of ALLAH!
#Mahdi Salehi

class Node:
    "Node for Linked List."
    def __init__(self, val) -> None:
        self.val = val
        self.next = self
        self.prev = self
class LinkedList:
    "Linked List"
    def __init__(self) -> None:
        self.last = None
        self.size = 0

    def __getitem__(self, index):
        if isinstance(index,int):
            if (not self.size) or (index < -1) or (index >= self.size):
                raise IndexError
            if index == -1 or index == self.size - 1:
                return self.last.val
            cur = self.last
            if index > (self.size >> 1):
                for i in range(self.size - index - 1):
                    cur = cur.prev
                return cur.val
            else:
                for i in range(index):
                    cur = cur.next
                return cur.next.val
        elif isinstance(index,slice):
            start, stop, step = index.indices(len(self))
            items = LinkedList()
            cur = self.last.next
            for i in range(start):
                cur = cur.next
            for i in range(start, stop):
                items.insert(cur.val)
                cur = cur.next
            return items
        else:
            raise TypeError
    
    def __setitem__(self, index, val):
        if (not self.size) or (index < -1) or (index >= self.size):
            raise IndexError
        if index == -1 or index == self.size - 1:
            self.last.val = val
            return
        cur = self.last
        if index > (self.size >> 1):
            for i in range(self.size - index - 1):
                cur = cur.prev
            cur.val = val
        else:
            for i in range(index):
                cur = cur.next
            cur.next.val = val
        # cur = self.last
        # for i in range(index):
        #     cur = cur.next
        # cur.next.val = val
    
    def __contains__(self, val):
        cur = self.last
        for i in range(self.size):
            if cur.val == val:
                return True
            cur = cur.next
        return False
    
    def __str__(self):
        if not self.size:
            return ""
        cur = self.last.next
        temp = '['+ str(cur.val)
        for i in range(self.size - 1):
            cur = cur.next
            temp += ', ' + str(cur.val)
        temp += ']'
        return temp
    
    def __iter__(self):
        return LLIterator(self)
    
    def __len__(self):
        return self.size

    def insert(self, val, index=-1):
        if (index < -1) or (index > self.size):
            raise IndexError
        new_node = Node(val)
        if not self.last:
            self.last = new_node
            self.size += 1
            return
        if index == -1 or index == self.size:
            new_node.next = self.last.next
            self.last.next.prev = new_node
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node
            self.size += 1
            return
        if not index:
            new_node.next = self.last.next
            new_node.next.prev = new_node
            new_node.prev = self.last
            self.last.next = new_node
            self.size += 1
            return
        cur = self.last
        if index > (self.size >> 1):
            for i in range(self.size - index):
                cur = cur.prev
        else:
            for i in range(index):
                cur = cur.next
        new_node.next = cur.next
        new_node.next.prev = new_node
        new_node.prev = cur
        cur.next = new_node
        self.size += 1
    
    def pop(self, index=-1):
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
        return node.val
    
    def get_index(self, val):
        cur = self.last.next
        for i in range(self.size):
            if cur.val == val:
                return i
            cur = cur.next
        raise KeyError

    def is_valid(self):
        cur = self.last
        for i in range(self.size):
            if cur.val != None:
                return True
            cur = cur.next
        return False
    
class LLIterator:
    """Iterator for Linked List."""
    def __init__(self, object):
        self.len = len(object)
        self.cur = object.last
        if (self.len):
            self.cur = self.cur.next

    def __next__(self):
        if self.len:
            val = self.cur.val
            self.cur = self.cur.next
            self.len -= 1
            return val
        else:
            raise StopIteration