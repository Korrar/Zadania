

class Linklist:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __getitem__(self, item):
        i = 0
        if self.tail == self.head:
            return self.tail.data
        else:
            trav = self.head
            while trav != self.tail:
                if i == item:
                    return trav.data
                i = i + 1
            if trav == self.tail:
                return self.tail.data
            else:
                raise Exception

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

    def remove(self):
        if self.size == 0:
            return None
        else:
            save = self.head
            self.head = self.head.next
            self.size = self.size - 1
            return save.data

class QueQue:
    def __init__(self):
        self.list = Linklist()

    def size(self):
        return self.list.size_o()

    def deque(self):
        return self.list.remove()

    def enque(self, elem):
        self.list.append(elem)


class Square:
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.lis = []
        self.start_row = 0
        self.start_col = 0
        self.rq = QueQue()
        self.cq = QueQue()

        self.steps = 0
        self.node_left = 1
        self.node_next = 0
        self.end = False
        self.visited = []

        self.d_row = [-1, 1, 0, 0]
        self.d_col = [0, 0, 1, -1]

    def load(self):
        i = 0
        with open('matrix.txt', "r") as file:
            for line in file:
                if i == 0:
                    leng_of_line = len(line) - 1
                    self.lis = [None] * int(len(line)-1)
                    self.rows = leng_of_line
                    self.columns = leng_of_line
                j = 0
                li = [None] * leng_of_line
                for let in line:
                    if let == "3":
                        self.start_row = i
                        self.start_col = j
                    if let == "\n":
                        continue
                    li[j] = let
                    j = j + 1
                self.lis[i] = li
                i = i + 1
            self.visited = [[0 for x in range(self.rows)] for y in range(self.columns)]


    def check_near(self, row, col):
        for i in range(4):
            row2 = row + self.d_row[i]
            col2 = col + self.d_col[i]

            if row2 < 0 or col2 < 0:
                continue
            if row2 >= self.rows or col2 >= self.columns:
                continue
            if self.visited[row2][col2]:
                continue
            if self.lis[row2][col2] == '1':
                continue
            self.rq.enque(row2)
            self.cq.enque(col2)
            self.visited[row2][col2] = True
            self.node_next = self.node_next + 1

    def go_look(self):
        self.rq.enque(self.start_row)
        self.cq.enque(self.start_col)
        self.visited[self.start_row][self.start_col] = True
        print(self.visited)

        while self.cq.size() > 0:
            row = self.rq.deque()
            col = self.cq.deque()

            if self.lis[row][col] == '2':
                self.end = True
                break
            self.check_near(row, col)
            self.node_left = self.node_left - 1
            if self.node_left == 0:
                self.node_left = self.node_next
                self.node_next = 0
                self.steps = self.steps + 1
        if self.end:
            return self.steps
        return False



s = Square()
s.load()
print(s.go_look())
