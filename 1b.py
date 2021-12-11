
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


def threes_larger_than_previous(lines):
    n = 0
    curr_three = 0
    prev_three = 0
    for i in range(2, len(lines)):
        curr_three = lines[i-2] + lines[i-1] + lines[i]
        print(curr_three)
        if prev_three:
            if curr_three > prev_three:
                n += 1

        prev_three = curr_three

    return n


def main():

    test_lines = get_lines('data/1_test.txt')
    assert len(test_lines) == 10
    assert n_of_larger_than_previous(test_lines) == 7

    assert threes_larger_than_previous(test_lines) == 5

    lines = get_lines('data/1.txt')
    n = threes_larger_than_previous(lines)

    print(n)

if __name__ == "__main__":
    main()
