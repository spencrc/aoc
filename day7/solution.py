import sys

def main():
    beam_columns = list()
    splits = 0
    with open(sys.argv[1]) as file:
        lines_list = file.read().splitlines()
        line_len = len(lines_list[0])
        for i in range(line_len):
            char = lines_list[0][i]
            if char == "S":
                beam_columns.append(i)
        for i in range(1, len(lines_list)):
            line = lines_list[i]
            to_remove = list()
            for j in beam_columns:
                char = line[j]
                if char == "^":
                    if not (j-1) in beam_columns:
                        beam_columns.append(j-1)
                    if not (j+1) in beam_columns:
                        beam_columns.append(j+1)
                    to_remove.append(j)
            for val in to_remove:
                beam_columns.remove(val)
                splits += 1

    print(splits)

if __name__ == "__main__":
    main()