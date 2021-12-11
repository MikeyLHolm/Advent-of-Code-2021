
def get_lines(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [int(line.rstrip()) for line in lines]

    return lines


def n_of_larger_than_previous(lines):
    n = 0
    tmp = 0
    for line in lines:
        if tmp:
            if line > tmp:
                n += 1

        tmp = line

    return n


def main():
    test_lines = get_lines('data/1_test.txt')
    assert len(test_lines) == 10
    assert n_of_larger_than_previous(test_lines) == 7

    lines = get_lines('data/1.txt')
    n = n_of_larger_than_previous(lines)

    print(n)

if __name__ == "__main__":
    main()
