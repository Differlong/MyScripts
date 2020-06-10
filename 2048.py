import random
import time


class Board(object):
    def __init__(self):
        self._width = 4
        self._height = 4
        self._matrix = None
        self.init_board()

    def init_board(self):
        self._matrix = list()
        for i in range(self._height):
            row = list()
            for j in range(self._width):
                row.append(0)
            self._matrix.append(row)
        self.random_add_more()
        self.random_add_more()

    def random_add_more(self):
        num = self.space_num
        if num == 0:
            self.game_over()
            return -1
        rd = random.randint(1, num)
        new_num = 2 if random.randint(0, 100) < 90 else 4
        print(num, rd, new_num)
        for i in range(self._height):
            for j in range(self._width):
                if self._matrix[i][j] == 0:
                    rd -= 1
                    if rd == 0:
                        self._matrix[i][j] = new_num
                        return 0
        if rd > 0:
            print("Something Wrong")
            # 那就直接重新塞一个进去
            for i in range(self._height):
                for j in range(self._width):
                    if self._matrix[i][j] == 0:
                        self._matrix[i][j] = new_num
                        return 0

    def show(self):
        print(self)

    def __str__(self):
        return "\n".join(map(str, self._matrix))

    def __repr__(self):
        return self.__str__()

    def is_game_over(self):
        # 动不了了 + 或者完全塞满了。
        if self.space_num > 0:
            return False
        # 每个和身边的都不一样
        for i in range(self._width):
            for j in range(self._height):
                if i + 1 < self._width and self._matrix[i][j] == self._matrix[i + 1][j]:
                    return False
                if j + 1 < self._height and self._matrix[i][j] == self._matrix[i][j + 1]:
                    return False
        return True

    def game_over(self):
        print("Game over!")
        exit(0)

    @staticmethod
    def transfor(lst):
        new_list = []
        old = -1
        for i in lst:
            if i == 0:
                continue
            elif i == old:
                new_list.append(2 * old)
                old = -1
            else:
                if old > 0:
                    new_list.append(old)
                old = i
        if old > 0:
            new_list.append(old)
        for i in range(len(lst) - len(new_list)):
            new_list.append(0)
        change = True if lst != new_list else False
        return change, new_list

    def up_merge(self):
        print("up_merge: ")
        change = False
        for i in range(self._width):
            row = []
            for j in range(self._height):
                row.append(self._matrix[j][i])
            tmp_change, new_list = self.transfor(row)
            change = change or tmp_change
            for j in range(self._height):
                self._matrix[j][i] = new_list[j]
        return change

    def down_merge(self):
        print("down_merge: ")
        change = False
        for i in range(self._width):
            row = []
            for j in range(self._height - 1, -1, -1):
                row.append(self._matrix[j][i])
            tmp_change, new_list = self.transfor(row)
            change = change or tmp_change
            for j in range(self._height):
                self._matrix[j][i] = new_list[self._height - 1 - j]
        return change

    def left_merge(self):
        print("left_merge: ")
        change = False
        for i in range(self._height):
            row = []
            for j in range(self._width):
                row.append(self._matrix[i][j])
            tmp_change, new_list = self.transfor(row)
            change = tmp_change or tmp_change
            for j in range(self._width):
                self._matrix[i][j] = new_list[j]
        return change

    def right_merge(self):
        print("right_merge: ")
        change = False
        for i in range(self._height):
            row = []
            for j in range(self._width - 1, -1, -1):
                row.append(self._matrix[i][j])
            tmp_change, new_list = self.transfor(row)
            change = change or tmp_change
            for j in range(self._width):
                self._matrix[i][j] = new_list[self._height - 1 - j]
        return change

    def loop(self):
        while not self.is_game_over():
            self.random_add_more()
            self.show()
            self.choose()
            self.show()

    def choose(self):
        key = input("Input the merge direction: ")
        change = False
        if key in ["w"]:
            change = self.up_merge()
        elif key in ["s"]:
            change = self.down_merge()
        elif key in ["a"]:
            change = self.left_merge()
        elif key in ["d"]:
            change = self.right_merge()
        elif key in ["q"]:
            self.game_over()
            change = True
        else:
            print("wrong key: ", key)
        if not change:
            print("Choose Again: ")
            self.choose()
    @property
    def max_num(self):
        return max(map(max, self._matrix))

    @property
    def space_num(self):
        return sum(map(lambda x: x.count(0), self._matrix))

    def win(self):
        return self.max_num >= 2048


if __name__ == "__main__":
    board = Board()
    board.loop()
