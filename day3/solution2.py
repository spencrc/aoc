import sys

def list_into_integer(digits: list) -> int:
    sum = 0
    for i in range(12):
        sum += digits[-(i+1)] * pow(10, i)
    return sum

def main():
    with open(sys.argv[1]) as file:
        lines_list = file.read().splitlines()
        sum = 0
        for line in lines_list:
            digits = list()
            for i in range(12):
                digits.append(int(line[i]))
            
            max_int = list_into_integer(digits)
            max_digits = digits

            for i in range(12, len(line)):
                cur = int(line[i])

                for j in range(12):
                    candidate_digits = digits.copy()
                    candidate_digits.pop(j)
                    candidate_digits.append(cur)
                    candidiate_number = list_into_integer(candidate_digits)
                    if max_int < candidiate_number:
                        max_int = candidiate_number
                        max_digits = candidate_digits
                digits = max_digits

            sum += list_into_integer(digits)
        print("The answer to part 2 for the given input is: ", sum)

if __name__ == "__main__":

    main()
