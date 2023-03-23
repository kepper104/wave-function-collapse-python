from random import choice
from pygametest import GridWindow
from time import sleep


class WaveFunctionCollapse:
    def __init__(self, field_size, grid_window=None):
        self.rules = {
            4: {3, 4},  # mountains
            3: {4, 3, 2},  # forest
            2: {3, 2, 1},  # field
            1: {2, 1}  # water
        }

        self.window = grid_window
        self.changed = list()
        self.field = list()
        # Generating field will all cells in superpositions
        for i in range(field_size):
            line = list()
            for j in range(field_size):

                line.append(list(range(1, 5)))
            self.field.append(line)

        self.field_size = field_size
        self.to_collapse = list()
        self.print()
        self.choose(2, 2, [4])
        print("------------------------------")
        self.print()
        print("------------------------------")

        self.cycle()

    def cycle(self):
        min_x, min_y, e = self.find_lowest_entropy()
        self.collapse(min_x, min_y)

        self.propagate(min_x, min_y)

    def print(self):
        for i in self.field:
            print(i)

    def find_lowest_entropy(self):
        minn = (0, 0, 100)
        for x in range(self.field_size):
            for y in range(self.field_size):
                cur = self.field[x][y]

                if type(cur) is int:
                    print("int!")
                    continue
                if len(cur) != 4:
                    print("isnt 4:", cur ,x, y)
                if minn[2] > len(cur) >= 1:
                    print("updated minn", cur)
                    minn = (x, y, len(cur))
        print(minn)
        return minn

    def collapse(self, x, y):
        if len(self.field[x][y]) == 1:
            self.field[x][y] = self.field[x][y][0]
        elif len(self.field[x][y]) == 0:
            print("Error at", x, y)
        else:
            rand_choice = choice(self.field[x][y])
            print(f"Chose {rand_choice} from {self.field[x][y]} at {x}, {y}")

            self.field[x][y] = rand_choice

    def propagate(self, x, y):
        self.to_collapse.append((x, y))
        self.changed.clear()
        while len(self.to_collapse) > 0:
            current = self.to_collapse.pop(0)
            self.changed.append(current)

            if self.window is not None:
                if type(self.field[current[0]][current[1]]) != int:
                    self.window.change_value(current[0], current[1], len(self.field[current[0]][current[1]]))
                self.window.cycle_color(current[0], current[1])
                self.window.external_update()

                sleep(0.5)

            adjacent_cells = self.get_adjacent_cells(*current)
            for i in adjacent_cells:
                # print(self.field[current[0]][current[1]])
                # print(list)
                iterate = list()
                a = self.field[current[0]][current[1]]
                if type(a) == int:
                    iterate.append(a)
                else:
                    iterate.extend(a)
                possible_variants = set()

                for possibility in iterate:
                    rule_set = set()
                    b = self.field[i[0]][i[1]]
                    # print("b", b)
                    if type(b) == int:
                        rule_set.add(b)
                    else:
                        for j in b:
                            rule_set.add(j)
                    # print(rule_set)
                    for j in self.rules[possibility].intersection(rule_set):
                        possible_variants.add(j)
                c = set()
                current_adjacent = self.field[i[0]][i[1]]
                if type(current_adjacent) == int:
                    c.add(current_adjacent)
                else:
                    for j in current_adjacent:
                        c.add(j)
                self.field[i[0]][i[1]] = list(c.intersection(possible_variants))
                if i not in self.to_collapse and i not in self.changed:
                    self.changed.append(i)
                    self.to_collapse.append(i)
            # self.print()
            # print(self.to_collapse)
            # input("continue?")
            # print("------------------------")
        # self.choose(x, y, self.field[x][y][0])
        print("-------------------------------------", self.to_collapse)
        self.print()

    def choose(self, x, y, choice):
        # if choice not in self.field[y][x]:
        #     return "Choice is not valid!"
        self.field[y][x] = choice
        return f"Chose {choice} from {self.field[y][x]}"

    def constrain(self, x, y):
        pass

    def is_solved(self):
        for x in range(self.field_size):
            for y in range(self.field_size):
                if len(self.field[y][x]) > 1:
                    return False
        return True

    def get_adjacent_cells(self, x, y):
        res = list()
        if x > 0:
            res.append((x - 1, y))
        if y > 0:
            res.append((x, y - 1))
        if x < self.field_size - 1:
            res.append((x + 1, y))

        if y < self.field_size - 1:
            res.append((x, y + 1))
        return res


def main():
    window = GridWindow(5, 50)
    WFC = WaveFunctionCollapse(5, window)

    WFC.choose(2, 2, 1)
    WFC.print()
    print("------------------------")

    WFC.propagate(2, 2)
    WFC.propagate(3, 2)
    # for index, i in enumerate(a):
    #     print(WFC.choose(i[0], i[1], index))
    # WFC.print()

    # while not WFC.isSolved():


if __name__ == "__main__":
    main()