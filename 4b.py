import numpy as np


class bingo_table:

    def __init__(self, five_rows) -> None:
        self.bingo = False
        self.sum = 0
        self.table = self.create_table(five_rows)
        self.visited = np.full((5, 5), False)


    def create_table(self, five_rows):
        table = []
        for i in range(5):
            row = list(filter(None, five_rows[i].split(' ')))
            tmp = []
            for j in range(0, len(row)):
                tmp.append(row[j])
            table.append(tmp)

        return np.array(table)

    def update_visited(self, table, visited, drawn):
        for i in range(5):
            for j in range(5):
                if drawn == table[i][j]:
                    visited[i][j] = True

    def is_bingo(self, visited_table):
        # check row
        for i in visited_table:
            for j in i:
                if j == False:
                    break
            else:
                return True

        # check column
        for i in range(5):
            for j in range(5):
                if visited_table[j][i] == False:
                    break
            else:
                return True

        return False


    def sum_of_not_visited(self, table, visited):
        self.sum = 0
        for i in range(5):
            for j in range(5):
                if visited[i][j] == False:
                    self.sum += int(table[i][j])

        return self.sum


def read_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines


def get_drawn_numbers(data):
    return np.array(data[0].split(','))


def create_tables(data):
    tables = []
    for i in range(0, len(data), 6):
        tables.append(bingo_table(data[i:i+5]))

    return tables


def check_last_to_bingo(tables):
    sum_bingos = 0
    for table in tables:
        if table.bingo:
            sum_bingos += 1

    if sum_bingos == len(tables) - 1:
        for table in tables:
            if not table.bingo:
                return True, table

    return False, None

def bingo_loop(drawn, tables):
    for nbr in drawn:
        check, last_table = check_last_to_bingo(tables)
        if check:
            last_table.update_visited(last_table.table, last_table.visited, nbr)
            # continue till the last table hits bingo as well
            if not last_table.is_bingo(last_table.visited):
                continue
            break
        for table in tables:
            table.update_visited(table.table, table.visited, nbr)
            if table.is_bingo(table.visited):
                table.bingo = True

    sum = last_table.sum_of_not_visited(last_table.table, last_table.visited)
    return sum*int(nbr)


def main():

    # test set
    test_data = read_input('data/4_test.txt')
    test_drawn = get_drawn_numbers(test_data)
    tables = create_tables(test_data[2:])
    test_res = bingo_loop(test_drawn, tables)
    assert test_res == 1924

    # real input
    data = read_input('data/4.txt')
    drawn = get_drawn_numbers(data)
    tables = create_tables(data[2:])
    # print(f'Drawn numbers are: {drawn}')
    res = bingo_loop(drawn, tables)
    print(f'Multiplication result: {res}')


if __name__ == "__main__":
    main()
