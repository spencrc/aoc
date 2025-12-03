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
                if (num_digits == 1):
                    # 1 digit numbers need to be skipped entirely (always valid)
                    continue

                accepted_list = list()
                accepted_list.append(stringified_n[0])

                for i in range (1, num_digits):
                    cur = stringified_n[i]
                    # stringify accepted_list, then repeat it as many times as we can fit
                    if "".join(accepted_list) * (num_digits // len(accepted_list)) == stringified_n:
                        invalid_sum += n
                        break
                    else:
                        accepted_list.append(cur)

        print("The answer to part 2 for the given input is:", invalid_sum)


if __name__ == "__main__":
    main()