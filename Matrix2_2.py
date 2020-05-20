"""Load two 2-dimensional matrices from file (binary: 0 or 1 per pixel). Check if smaller one pattern can be found in
larger one, """


class Square:
    def __init__(self):
        self.N = 3
        self.lis = [None] * self.N

    def load(self):
        i = 0
        with open('matrix.txt', "r") as file:
            for line in file:
                if i == 0:
                    leng_of_line = len(line) - 1
                    self.lis = [None] * int(len(line)-1)
                j = 0
                li = [None] * leng_of_line
                for let in line:
                    if let == "\n":
                        continue
                    li[j] = let
                    j = j + 1
                self.lis[i] = li
                i = i + 1

    def go(self):
        pass




s = Square()
s.load()
print(s.lis[0][0])

