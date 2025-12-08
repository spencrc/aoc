import sys

def solve_part_1(all_operands: list, operators: list, num_operands_per_line: int) -> int:
    total = 0
    for i in range(num_operands_per_line):
        res = 0
        for line_operands in all_operands:
            if operators[i] == "+":
                res += line_operands[i]
            elif operators[i] == "*":
                if res == 0:
                    res = 1
                res *= line_operands[i]
        total += res
    return total

def solve_part_2(all_operands: list, operators: list, num_operands_per_line: int) -> int:
    pass

def main():
    all_operands = list()
    operators = list()
    num_operands_per_line = None

    with open(sys.argv[1]) as file:
        lines_list = file.read().splitlines()
        for i in range(len(lines_list) - 1):
            split_line = lines_list[i].split()

            if not num_operands_per_line:
                num_operands_per_line = len(split_line)

            line_operands = [int(x) for x in split_line]
            all_operands.append( line_operands )
        operators = lines_list[-1].split()

    answer1 = solve_part_1(all_operands, operators, num_operands_per_line)
    solve_part_2(all_operands, operators, num_operands_per_line)

    print(answer1)


if __name__ == "__main__":
    main()