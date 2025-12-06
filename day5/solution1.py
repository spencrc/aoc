import sys

def main():
    handle_ranges = True
    ranges = list()
    num_fresh = 0
    with open(sys.argv[1]) as file:
        lines_list = file.read().splitlines()
        for line in lines_list:
            if not line:
                handle_ranges = False
            elif handle_ranges:
                tokenized_line = line.split("-")

                lower_limit = int(tokenized_line[0])
                upper_limit = int(tokenized_line[1])
                
                ranges.append( (lower_limit, upper_limit) )
            else:
                n = int(line)
                for range in ranges:
                    if (n >= range[0] and n <= range[1]):
                        num_fresh += 1
                        break
    print(num_fresh)

if __name__ == "__main__":
    main()