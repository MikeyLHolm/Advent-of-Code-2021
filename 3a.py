
def get_more_common_nbr(dict_key):
    if dict_key['0'] > dict_key['1']:
        return '0'
    return '1'

def ugly_str_former(values):
    bin_str = ''

    for i in range(12):
        bin_str += get_more_common_nbr(values[i])
        print(bin_str)

    return bin_str

def read_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def get_gamma_rate(lines):
    values = {
        0: {'0': 0, '1': 0},
        1: {'0': 0, '1': 0},
        2: {'0': 0, '1': 0},
        3: {'0': 0, '1': 0},
        4: {'0': 0, '1': 0},
        5: {'0': 0, '1': 0},
        6: {'0': 0, '1': 0},
        7: {'0': 0, '1': 0},
        8: {'0': 0, '1': 0},
        9: {'0': 0, '1': 0},
        10: {'0': 0, '1': 0},
        11: {'0': 0, '1': 0},
        12: {'0': 0, '1': 0},
    }

    for line in lines:

        for i, nbr in enumerate(line):
            print(i, nbr, type(nbr))
            values[i][nbr] += 1

    return ugly_str_former(values)


def get_epsilon_rate(gamma_rate):
    """reverse numbers in gamma rate"""
    epsilon_rate = ''
    for nbr in gamma_rate:
        if nbr == '0':
            epsilon_rate += '1'
        else:
            epsilon_rate += '0'

    return epsilon_rate

def get_power_consumption(gamma, epsilon):
    pc = int(gamma, 2) * int(epsilon, 2)
    return pc

def main():
    # test_lines = read_input('data/3_test.txt')
    # assert len(test_lines) == 12

    # test_gr_bin = get_gamma_rate(test_lines)
    # assert test_gr_bin == '10110'  # 22

    # test_eps_bin = get_epsilon_rate(test_gr_bin)
    # assert test_eps_bin == '01001'  # 9

    # assert get_power_consumption(test_gr_bin, test_eps_bin) == 198

    lines = read_input('data/3.txt')
    assert len(lines) == 1000

    gr_bin = get_gamma_rate(lines)
    eps_bin = get_epsilon_rate(gr_bin)
    print(get_power_consumption(gr_bin, eps_bin))


if __name__ == "__main__":
    main()
