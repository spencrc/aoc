import sys

def parse(input: str) -> int:
    first_letter = input[0]
    n = int(input[1:])
    if (first_letter == "L"):
        return -1 * n
    else:
        return n

def shift(cur: int, n: int) -> int:
    if cur + n <= 0:
        return (100 - (-cur - n)) % 100
    else:
        return (cur + n) % 100
    
def zero_passes(cur: int, n: int) -> int:
    if shift(cur, n) == 0 and abs(cur + n) < 100:
        return 1
    else:
        res = abs(cur + n) // 100
        if cur == 0:
            return res
        elif cur + n < 0:
            return res + 1
        else:
            return res
        
def main():
    cur = 50
    answer_one = 0
    answer_two = 0

    with open(sys.argv[1]) as file:
        linelist = file.read().splitlines()
        for line in linelist:
            n = parse(line)
            answer_two += zero_passes(cur, n)
            cur = shift(cur, n)
            if cur == 0:
                answer_one += 1

    print("The answer to part 1 for the given input is: ", answer_one)
    print("The answer to part 2 for the given input is: ", answer_two)

if __name__ == "__main__":
    main()