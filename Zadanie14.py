


class Linklist:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

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
        return trav.data

    class Node:
        def __init__(self, next, prev, data):
            self.next = next
            self.prev = prev
            self.data = data

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



class Graph:
    def __init__(self, filename):
        self.filename = filename
        self.graph = []
        self.graph2 = []
        self.graph_list = []
        self.number_of_nodes = 0
        self.counter = 0

        self.visited = []
        self.components = []

    def load(self):
        i = 1
        with open('{}'.format(self.filename), "r") as file:
            number_of_nodes = 7

        self.number_of_nodes = 7
        self.visited = [False] * number_of_nodes
        self.graph = [None] * (number_of_nodes * 2)
        self.graph2 = [None] * (number_of_nodes * 2)
        self.components = [None] * number_of_nodes
        self.graph_list = [Linklist() for k in range(number_of_nodes *2)]

        with open('{}'.format(self.filename), "r") as file:
            for line in file:
                j = 0
                for let in line:
                    if let == "," or let == "\n":
                        continue
                    if j == 0:
                        self.graph[i] = let
                        self.graph2[i + 1] = let
                    if j == 1:
                        self.graph[i + 1] = let
                        self.graph2[i] = let
                    j = j+1
                i = i + 2

        for i in range(self.number_of_nodes*2):
            u = self.graph[i]
            v = self.graph2[i]
            if u and v:
                self.graph_list[int(u)].append(int(v))


    def find_comp(self):
        for i in range(self.number_of_nodes):
            if not self.visited[i]:
                self.counter = self.counter + 1
                self.check(i)
        return self.counter, self.components

    def check(self, at):
        self.visited[at] = True
        self.components[at] = self.counter
        """
        for nex in self.graph_list[at]:
            print(nex)
            if not self.visited[nex]:
                self.check(nex)

        """
        for i in range(self.graph_list[at].size_o()):
            if not self.visited[self.graph_list[at][i]]:
                self.check(self.graph_list[at][i])


g = Graph('gr')
g.load()
print(g.find_comp())

