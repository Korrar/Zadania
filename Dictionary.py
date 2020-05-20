class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __getitem__(self, item):
        i = 0
        if self.head == self.tail:
            return self.head
        trav = self.head
        while trav != self.tail:
            if i == item:
                return trav.data
            trav = trav.next
            i = i + 1
        if trav == self.tail:
            return self.tail.data

    class Node:
        def __init__(self, prev, next, data):
            self.prev = prev
            self.next = next
            self.data = data

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def append(self, element):
        if self.is_empty():
            self.head = self.tail = self.Node(None, None, element)
        else:
            self.tail.next = self.Node(self.tail, None, element)
            self.tail = self.tail.next
        self.size = self.size +1




class Tup:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = hash(key)

class HashMap:
    def __init__(self):
        self.default_size = 3
        self.table = LinkedList()

    def add(self, key, value):
        entry = Tup(key, value)
        index = entry.hash
        return self.insert(entry, index)

    def insert(self, entry, index):
        bucket = self.table[index]




do = LinkedList()
do.append('adsdasdad')
do.append('ad33sdasdad')
print(do[1])


