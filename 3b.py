from copy import deepcopy


def read_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines


def most_common_value(lines, i):
    zero = 0
    one = 0
    for line in lines:
        if line[i] == '0':
            zero += 1
        else:
            one += 1

    return '0' if zero > one else '1'


def split_list(lines, i):
    co2_scrubber_list = []
    oxygen_generator_list = deepcopy(lines)
    mcv = most_common_value(lines, i)
    for line in lines:
        if not line[i] == mcv:
            lst_i = oxygen_generator_list.index(line)
            co2_scrubber_list.append(oxygen_generator_list.pop(lst_i))

    return oxygen_generator_list, co2_scrubber_list


def get_oxygen_rating(data_list, i):
    list_len = len(data_list)
    if list_len == 1:
        return int(data_list[0], 2)

    data_cpy = deepcopy(data_list)
    mcv = most_common_value(data_list, i)
    for line in data_list:
        if not line[i] == mcv:
            lst_i = data_cpy.index(line)
            data_cpy.pop(lst_i)

    return get_oxygen_rating(data_cpy, i + 1)


def get_co2_rating(data_list, i):
    list_len = len(data_list)
    if list_len == 1:
        return int(data_list[0], 2)

    data_cpy = deepcopy(data_list)
    mcv = most_common_value(data_list, i)
    for line in data_list:
        if line[i] == mcv:
            lst_i = data_cpy.index(line)
            data_cpy.pop(lst_i)

    return get_co2_rating(data_cpy, i + 1)


def get_life_support_rating(lines):
    co2_scrubber_list = []
    oxygen_generator_list = []
    oxygen_generator_list, co2_scrubber_list = split_list(lines, 0)

    og_r = get_oxygen_rating(oxygen_generator_list, 1)
    print(og_r)
    co2s_r = get_co2_rating(co2_scrubber_list, 1)
    print(co2s_r)

    return og_r * co2s_r


def main():
    test_lines = read_input('data/3_test.txt')
    assert len(test_lines) == 12

    life_support_rating = get_life_support_rating(test_lines)
    print(f'life support rating with test data: [{life_support_rating}]')
    assert life_support_rating == 230

    lines = read_input('data/3.txt')
    assert len(lines) == 1000

    life_support_rating = get_life_support_rating(lines)
    print(f'life support rating: [{life_support_rating}]')


if __name__ == "__main__":
    main()
