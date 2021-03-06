
class Linklist:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __getitem__(self, item):

        if self.size == 0:
            return None
        if self.head == self.tail:
            return self.head.data
        trav = self.head
        for i in range(0, int(item)):
            if i == item:
                return trav.data
            trav = trav.next
        return trav.data

    def __setitem__(self, key, value):
        i = 0
        if self.size == 0:
            raise Exception('empty list')
        trav = self.head
        while trav != self.tail:
            if i == key:
                trav.data = value
                break
            trav = trav.next
            i = i + 1

    def __repr__(self):
        strin = ''
        trav = self.head
        while trav != self.tail:
            print(trav)
            strin = strin + str(trav)
            trav = trav.next
        strin = strin + str(self.tail)
        return strin

    class Node:
        def __init__(self, next, prev, data):
            self.next = next
            self.prev = prev
            self.data = data

        def __repr__(self):
            return str(self.data)

    def size_o(self):
        return self.size

    def empty(self):
        return self.size == 0

    def append(self, data):
        if self.size == 0:
            self.head = self.tail = self.Node(None, None, data)
        else:
            self.tail.next = self.Node(None, self.tail, data)
            self.tail = self.tail.next
        self.size = self.size + 1


class PiorQueQue:
    def __init__(self):
        self.size = 0
        self.list = Linklist()

    def add(self, element):
        if element is None:
            raise Exception('no null elements')
        else:
            self.list.append(element)
        self.swim(self.size)
        self.size = self.size + 1

    def empty(self):
        return self.size == 0

    def poll(self):
        if self.empty():
            return None
        self.size = self.size - 1
        removed = self.list[0]
        self.swap(0, self.size)
        self.list[self.size] = None
        self.sink(0)
        self.swim(0)
        return removed

    def swap(self, i, j):
        node1 = self.list[i]
        node2 = self.list[j]

        self.list[i] = node2
        self.list[j] = node1

    def less(self, i, j):
        node1 = self.list[i]
        node2 = self.list[j]
        return node1 <= node2

    def swim(self, k):
        parent = ((k - 1)/2)

        while k > 0 and self.less(k, parent):
            self.swap(parent, k)
            k = parent
            parent = (k-1)/2

    def sink(self, k):
        while True:
            left = 2 * k + 1
            right = 2 * k + 2
            smallest = left
            if right < self.size and self.less(right, left):
                smallest = right
            if left >= self.size or self.less(k, smallest):
                break
            self.swap(smallest, k)
            k = smallest


class Graph:
    def __init__(self, filename):
        self.previous = []
        self.filename = filename
        self.graph = []
        self.graph2 = []
        self.graph_list = []
        self.number_of_nodes = 0
        self.starting_node = 3
        self.finish_node = 4

    def load(self):
        num = 0
        i = 0
        j = 0
        with open('{}'.format(self.filename), "r") as file:
            for line in file:
                word = ''
                for let in line:
                    if let == "\n":
                        break
                    if let == ",":
                        if int(num) < int(word):
                            num = int(word)
                        word = ''
                        j = j + 1
                        continue
                    word = word + let
                if int(num) < int(word):
                    num = int(word)
                i = i + 1
            number_of_nodes = num + 1
        self.number_of_nodes = number_of_nodes
        self.graph = [None] * number_of_nodes
        self.graph2 = [None] * number_of_nodes
        self.visited = [False] * number_of_nodes
        self.previous = [None] * number_of_nodes
        self.infinity = 9999999
        self.distance = [self.infinity] * number_of_nodes

        self.graph_list = [Linklist() for k in range(number_of_nodes)]
        i = 0
        with open('{}'.format(self.filename), "r") as file:
            for line in file:
                word = ''
                j = 0
                for let in line:
                    if let == "\n":
                        break
                    if let == ",":
                        if j == 0:
                            self.graph[i] = int(word)
                        if j == 1:
                            self.graph2[i] = int(word)
                        word = ''
                        j = j + 1
                        continue
                    word = word + let
                self.graph2[i] = [self.graph2[i], int(word)]
                i = i + 1

        for i in range(self.number_of_nodes):
            u = self.graph[i]
            v = self.graph2[i]
            if u is not None and v is not None:
                self.graph_list[u].append(v)


def shortest_path(graph, number, start, ):
    visited = [False] * number
    infinity = 999999999
    distance = [infinity] * number
    previous = [None] * number
    distance[start] = 0
    pq = PiorQueQue()
    pq.add((start, 0))
    while pq.size != 0:
        index, min = pq.poll()
        visited[index] = True

        for edge in graph:
            for i in range(edge.size_o()):
                try:
                    edge[i][0]
                except TypeError:
                    break
                if visited[edge[i][0]]:
                    continue
                new_dist = distance[index] + edge[i][1]
                if new_dist < distance[edge[i][0]]:
                    previous[edge[i][0]] = index
                    distance[edge[i][0]] = new_dist
                    pq.add((edge[i][0], new_dist))
    return (distance, previous)


def shortfurther(graph, number, start, end):
    distance, previous = shortest_path(graph, number, start)
    infinity = 999999999
    path = []
    if distance == infinity:
        return path
    at = end
    while at is not None:
        path.append(at)
        at = previous[at]
    return path


g = Graph('gr')
g.load()

print(shortfurther(g.graph_list, g.number_of_nodes, g.starting_node, g.finish_node))

