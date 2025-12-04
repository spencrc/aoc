import sys

def main():
    with open(sys.argv[1]) as file:
        lines_list = file.read().splitlines()
        sum = 0
        for line in lines_list:
            max_tens = int(line[0])
            max_ones = int(line[1])
            for i in range(2, len(line)):
                cur = int(line[i])
                if max_ones == 9 and max_tens == 9:
                    break
                if max_ones > max_tens:
                    max_tens = max_ones
                    max_ones = cur
                if cur > max_ones:
                    max_ones = cur
            sum += max_tens * 10 + max_ones
        print("The answer to part 1 for the given input is: ", sum)

if __name__ == "__main__":
    main()