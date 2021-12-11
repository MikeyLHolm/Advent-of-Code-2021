
def get_lines(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines


def get_new_position(lines):

    x = 0
    depth = 0
    aim = 0
    for line in lines:
        split_line = line.split()
        if split_line[0] == 'forward':
            depth += int(split_line[1]) * aim
            x += int(split_line[1])
        elif split_line[0] == 'down':
            aim += int(split_line[1])
        elif split_line[0] == 'up':
            aim -= int(split_line[1])

    return(x, depth)


def main():

    test_lines = get_lines('data/2_test.txt')
    assert len(test_lines) == 6
    x, d = get_new_position(test_lines)
    print(x * d)
    assert x * d == 900

    lines = get_lines('data/2.txt')
    assert len(lines) == 1000
    x, d = get_new_position(lines)

    print(x*d)

if __name__ == "__main__":
    main()
