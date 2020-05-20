class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __getitem__(self, item):
        i = 0
        if self.head == self.tail:
            return self.head.data
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


def hashi(key):
    ha = 0
    for h in key:
        ha = ha + ord(h)
    return ha % 256

class Tup:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = hashi(key)


class HashMap:
    def __init__(self):
        self.default_size = 256
        self.table = [None] * self.default_size

    def add(self, key, value):
        entry = Tup(key, value)
        index = entry.hash
        return self.insert(entry, index)

    def insert(self, entry, index):

        if self.table[index] is None:
            self.table[index] = LinkedList()
        self.table[index].append(entry)

    def get(self, key):
        key_str = key
        index = hashi(key)
        i = 0
        for key in self.table[index]:
            if self.table[index][i].key == key_str:
                print(self.table[index][i].value)
                break
            i = i+1




do = HashMap()
do.add('a','hello')
do.add('v','he222o')
do.get('v')
do.get('a')


