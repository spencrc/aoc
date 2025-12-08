import sys

def main():
    column_starts = list()
    all_operands = list()
    operators = list()
    num_operands_per_line = None

    with open(sys.argv[1]) as file:
        lines_list = file.read().splitlines()
        for i in range(len(lines_list[-1])):
            char = lines_list[-1][i];
            if char == "*" or char == "+":
                operators.append(char)
                column_starts.append(i)
        for i in range(len(lines_list) - 1):
            count = 0
            line = lines_list[i]
            row_operands = list()

            for j in range(len(line)):
                if j in column_starts:
                    if count + 1 < len(column_starts):
                        row_operands.append(line[j:column_starts[count+1]-1])
                        count += 1
                    else:
                        row_operands.append(line[j:])
            if not num_operands_per_line:
                num_operands_per_line = len(row_operands)
            all_operands.append(row_operands)

    verticals_list = list()
    for _ in range(num_operands_per_line):
        verticals_list.append( list() )

    for col in range(num_operands_per_line):
        for row in range(len(all_operands)):
            n = all_operands[row][col]
            stringified_n = str(n)
            num_digits = len(stringified_n)

            for _ in range(len(verticals_list[col]), num_digits):
                verticals_list[col].append(list())

            for digits_idx in range(num_digits):
                verticals_list[col][num_digits - digits_idx - 1].append(stringified_n[digits_idx])
    
    total = 0
    for i in range(len(verticals_list)):
        grouping = verticals_list[i]
        res = 0
        for numbers in grouping:
            n = int("".join(numbers).strip())
            if operators[i] == "+":
                res += n
            else:
                if res == 0:
                    res = 1
                res *= n
        total += res

    print(total)

if __name__ == "__main__":
    main()