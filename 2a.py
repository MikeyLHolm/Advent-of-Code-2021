
def get_lines(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines


def get_new_position(lines):

    x = 0
    y = 0
    for line in lines:
        split_line = line.split()
        if split_line[0] == 'forward':
            x += int(split_line[1])
        elif split_line[0] == 'down':
            y += int(split_line[1])
        elif split_line[0] == 'up':
            y -= int(split_line[1])

    return(x, y)


def main():

    test_lines = get_lines('data/2_test.txt')
    assert len(test_lines) == 6
    x, y = get_new_position(test_lines)

    assert x * y == 150

    lines = get_lines('data/2.txt')
    assert len(lines) == 1000
    x, y = get_new_position(lines)

    print(x*y)

if __name__ == "__main__":
    main()
