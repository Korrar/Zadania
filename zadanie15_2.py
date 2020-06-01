
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


class PiorityQue:
    def __init__(self, number):
        self.table = [None] * (number + 1)
        self.size = 0
        self.capacity = number + 1

    def insert(self, item):

        if self.capacity < self.size:
            raise Exception('overflow size')
        self.table[self.size] = item
        self.size = self.size + 1
        self.heap_up(self.size - 1)

    def compare(self, index, parent):
        node1 = self.table[index]
        node2 = self.table[int(parent)]
        if not node1 or not node2:
            return False
        return node1[1] < node2[1]

    def swap(self, i, j):
        if self.table[i] is not None:
            temp = list(self.table[i])
        else:
            temp = None
        self.table[i] = self.table[j]
        self.table[j] = temp

    def heap_up(self, index):

        parent = int((index - 1) / 2)
        if index > 0:
            while index > 0 and self.compare(index, parent):
                self.swap(parent, index)
                index = parent
                parent = (index - 1) / 2

    def heap_down(self, index):
        while True:
            left, right = self.get_child(index)
            small = left
            if right < self.size and self.compare(right, left):
                small = right
            if left >= self.size or self.compare(index, small):
                break
            self.swap(small, index)
            index = small

    def get_child(self, index):
        return 2 * index + 1, 2 * index + 2

    def poll(self):
        if self.size == 0:
            return None
        value = list(self.table[0])
        self.table[0] = self.table[self.size - 1]
        self.table[self.size -1] = None
        self.size = self.size - 1
        self.heap_down(0)
        return value


class Graph:
    def __init__(self, filename):
        self.previous = []
        self.filename = filename
        self.graph = []
        self.graph2 = []
        self.graph_list = []
        self.number_of_edges = 0
        self.number_of_nodes = 0

    def load(self):
        i = 0
        j = 0
        with open('{}'.format(self.filename), "r") as file:
            for line in file:

                i = i + 1
            number_of_edges = i
        self.number_of_edges = number_of_edges
        graph = [None] * self.number_of_edges
        graph2 = [None] * 3

        with open('{}'.format(self.filename), "r") as file:
            i = 0
            for line in file:
                word = ''
                j = 0
                for let in line:
                    if let == "\n":
                        break
                    if let == ",":
                        graph2[j] = int(word)
                        if int(word) > self.number_of_nodes:
                            self.number_of_nodes = int(word)
                        j = j + 1
                        word = ''
                        continue
                    word = word + let
                if word == '':
                    continue
                graph2[j] = int(word)
                graph[i] = [graph2[0], graph2[1], graph2[2]]
                i = i + 1
        print(number_of_edges)
        return graph


def shortest_path(start, graph , number_of_nodes):
    infinity = 99999999
    visited = [False] * (number_of_nodes + 1)
    previous = [None] * (number_of_nodes + 1)
    distance = [infinity] * (number_of_nodes + 1)
    distance[start] = 0
    pq = PiorityQue(number_of_nodes)
    pq.insert([start, 0])
    while pq.size != 0:
        index, min_val = pq.poll()
        visited[index] = True
        for i in range(graph[index].size):
            edge = graph[index][i]
            if visited[edge[0]]:
                continue
            new_distance = distance[index] + edge[1]
            if new_distance < distance[edge[0]]:
                previous[edge[0]] = index
                distance[edge[0]] = new_distance
                pq.insert([edge[0], new_distance])
    return distance, previous


def point_to_point(graph, number, start, end):
    distance, previous = shortest_path(start, graph, number)
    infinity = 99999999
    path = []
    if distance == infinity:
        return path
    at = end
    while at is not None:
        path.append(at)
        at = previous[at]
    return path

start = 0
end = 4

gr = Graph('gr')
graph = gr.load()
adj_list = [Linklist() for k in range(gr.number_of_nodes +1)]


for edge in graph:
    if edge:
        adj_list[edge[0]].append([edge[1], edge[2]])


print(point_to_point(adj_list, gr.number_of_nodes, start, end))




