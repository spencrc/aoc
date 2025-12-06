# i originally solved this problem using the naive, brute-force solution; however, it had an impossible wait time and took up an insane amount of
#  memory. as a result, i re-wrote the whole thing... and while researching to figure out *how* i could tackle this problem, i pretty much spoiled
#  it for myself by finding this stack overflow article: https://stackoverflow.com/a/78269169
#  very unfortunate T-T
import sys

def main():
    ranges = list()
    merged_ranges = []
    num_fresh_ids = 0
    with open(sys.argv[1]) as file:
        lines_list = file.read().splitlines()
        for line in lines_list:
            if not line:
                break
            tokenized_line = line.split("-")

            lower_limit = int(tokenized_line[0])
            upper_limit = int(tokenized_line[1])
            
            ranges.append( (lower_limit, upper_limit) )
    # we sort the ranges, that way ranges will be ordered and we only will need to care about the current range and last range when updating
    ranges.sort()
    # add the very first range to the list of merged ranges
    merged_ranges.append(ranges[0])
    # now we loop over every range!
    for i in range(1, len(ranges)):
        id_range = ranges[i]
        # if the current lower limit is greater than the (current) biggest upper limit,
        #   we append the current range since it's impossible for it to fall into any interval
        if id_range[0] > merged_ranges[-1][1]:
            merged_ranges.append(id_range)
        # we are going to replace the last range in the list of merged ranges with the current range,
        #  as the current range falls within the last range (since the list of ranges is sorted).
        #  when doing this we want the replacement to take the minimum of the two ranges for its lower bound
        #  and the maximum of the two ranges for its upper bound
        else:
            temp = merged_ranges.pop()
            merged_ranges.append( (min(temp[0], id_range[0]), max(temp[1], id_range[1]) ) )

    print(merged_ranges)

    for id_range in merged_ranges:
        lower_limit = id_range[0]
        upper_limit = id_range[1]
        num_fresh_ids += upper_limit - lower_limit + 1

    print(num_fresh_ids)

if __name__ == "__main__":
    main()