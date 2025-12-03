import sys

def main():
    with open(sys.argv[1]) as file:
        input = file.read()
        id_range_list = input.split(",")
        invalid_sum = 0
        for id_range in id_range_list:
            limits_list = id_range.split("-")

            lower_limit = int(limits_list[0])
            upper_limit = int(limits_list[1]) + 1
            
            for n in range(lower_limit, upper_limit):
                stringified_n = str(n)
                num_digits = len(stringified_n)
                # odd number of digits
                if (num_digits % 2 != 0):
                    continue
                else:
                    half_num_digits = num_digits // 2
                    same = True
                    for i in range(half_num_digits):
                        if stringified_n[i] != stringified_n[half_num_digits + i]:
                            same = False
                            break
                    if same:
                        invalid_sum += n
        print("The answer to part 1 for the given input is:", invalid_sum)


if __name__ == "__main__":
    main()