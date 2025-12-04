import sys

def main():
    output = list()
    marked_count = 0
    with open(sys.argv[1]) as file:
        lines_list = file.read().splitlines()
        for i in range(len(lines_list)):
            cur_line = lines_list[i]
            output_line = list()
            if i == 0:
                next_line = lines_list[i+1]

                for j in range(len(cur_line)):
                    if cur_line[j] == ".":
                        output_line.append(".")
                        continue

                    count = 0
                    if j != 0:
                        if cur_line[j-1] == "@": # looking left OR down-left
                            count += 1
                        if next_line[j-1] == "@":
                            count += 1
                    if j != len(cur_line) - 1:
                        if cur_line[j+1] == "@": # looking right OR down-right
                            count += 1
                        if next_line[j+1] == "@":
                            count += 1
                    if next_line[j] == "@": # looking down
                        count += 1

                    if count < 4:
                        output_line.append("x")
                        marked_count += 1
                    else:
                        output_line.append("@")
            elif i == len(lines_list) - 1:
                prev_line = lines_list[i-1]

                for j in range(len(cur_line)):
                    if cur_line[j] == ".":
                        output_line.append(".")
                        continue

                    count = 0
                    if j != 0:
                        if cur_line[j-1] == "@": # looking left OR up-left
                            count += 1
                        if prev_line[j-1] == "@":
                            count += 1
                    if j != len(cur_line) - 1:
                        if cur_line[j+1] == "@": # looking right OR up-right
                            count += 1
                        if prev_line[j+1] == "@":
                            count += 1
                    if prev_line[j] == "@": # looking up
                        count += 1

                    if count < 4:
                        output_line.append("x")
                        marked_count += 1
                    else:
                        output_line.append("@")
            else:
                next_line = lines_list[i+1]
                prev_line = lines_list[i-1]

                for j in range(len(cur_line)):
                    if cur_line[j] == ".":
                        output_line.append(".")
                        continue

                    count = 0
                    if j != 0:
                        if cur_line[j-1] == "@":
                            count += 1
                        if next_line[j-1] == "@":
                            count += 1
                        if prev_line[j-1] == "@": 
                            count += 1
                    if j != len(cur_line) - 1:
                        if cur_line[j+1] == "@":
                            count += 1
                        if next_line[j+1] == "@":
                            count += 1
                        if prev_line[j+1] == "@": 
                            count += 1
                    if next_line[j] == "@":
                        count += 1
                    if prev_line[j] == "@": # looking down OR up
                        count += 1

                    if count < 4:
                        output_line.append("x")
                        marked_count += 1
                    else:
                        output_line.append("@")
            output.append("".join(output_line))
    print("\n".join(output))
    print("\nThe number of accessible rolls is:", marked_count)

if __name__ == "__main__":
    main()