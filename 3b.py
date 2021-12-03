
def read_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines


def most_common_value(lines, i):
    zero = 0
    one = 0
    for line in lines:
        print(line)
        if line[i] == '0':
            zero += 1
        else:
            one += 1

    return '0' if zero > one else '1'


def foo(lines):
    line_len = len(lines[0])
    managed_list = []
    for i in range(line_len):
        if most_common_value(lines, i) == '1':
            print(most_common_value(lines, i))


def main():
    test_lines = read_input('data/3_test.txt')
    assert len(test_lines) == 12

    foo(test_lines)

    lines = read_input('data/3.txt')
    assert len(lines) == 1000

    oxygen_gen_r = 0
    co2_scrubber_r = 0
    life_support_rating = oxygen_gen_r * co2_scrubber_r
    # print(life_support_rating)




if __name__ == "__main__":
    main()
