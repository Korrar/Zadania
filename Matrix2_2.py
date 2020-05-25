"""Load two 2-dimensional matrices from file (binary: 0 or 1 per pixel). Check if smaller one pattern can be found in
larger one, """


def compare(bigger, smaller):
    rows_last = smaller.number_of_rows - 1
    columns_last = len(smaller.lis[0]) - 1
    j = 0
    for row2 in bigger.lis:
        i = 0
        for col in row2:
            if (i + columns_last) >= len(row2):
                continue
            if row2[i] == smaller.lis[0][0] \
                    and row2[i + columns_last] == smaller.lis[0][columns_last]\
                    and bigger.lis[rows_last+j][i] == smaller.lis[rows_last][0]\
                    and bigger.lis[rows_last+j][i + columns_last] == smaller.lis[rows_last][columns_last]:
                x = 0
                while True:
                    if x > rows_last:
                        return True
                    y = 0
                    while True:
                        if y > columns_last:
                            break
                        if not bigger.lis[j + x][i + y] == smaller.lis[x][y]:
                            break
                        y = y + 1
                    x = x + 1
            i = i + 1
        j = j + 1
    return False


class Square:
    def __init__(self, filename):
        self.lis = []
        self.filename = filename
        self.number_of_rows = 0

    def load(self):
        i = 0
        with open('{}'.format(self.filename), "r") as file:
            number = 0
            for l in file:
                number = number + 1

        with open('{}'.format(self.filename), "r") as file:
            for line in file:
                if i == 0:
                    leng_of_line = len(line) - 1
                    self.lis = [None] * number
                j = 0
                li = [None] * leng_of_line
                for let in line:
                    if let == "\n":
                        continue
                    li[j] = let
                    j = j + 1
                self.lis[i] = li
                i = i + 1
            self.number_of_rows = i



bigger = Square('matrix.txt')
smaller = Square('smaller')
bigger.load()
smaller.load()
print(compare(bigger, smaller))

