# i was completely stumped on this day. i got inspiration to use a DFS (assuming the input is a very weird DAG) from the youtube video below:
#  https://www.youtube.com/watch?v=-jleBmTQ9o0

import sys

def dfs_recursive(row: int, col: int, visited: list[int], height: int, width: int, lines_list: list[str]) -> int:
    # don't do unnecessary or possibly problematic work by traversing an already visited character
    if visited[row * width + col]:
        return visited[row * width + col]
    
    while row < height and lines_list[row][col] != "^":
        # we can keep going down without splitting
        row += 1

    # if we've reached the bottom, it's over. we return 1
    if row == height:
        return 1
    
    # don't do unnecessary or possibly problematic work by traversing an already visited character
    if visited[row * width + col]:
        return visited[row * width + col]

    # go right
    visited[row * width + col] += dfs_recursive(row, col + 1, visited, height, width, lines_list)
    # go left
    visited[row * width + col] += dfs_recursive(row, col - 1, visited, height, width, lines_list)

    return visited[row * width + col]

def dfs(height: int, width: int, starting_col: int, lines_list: list[str]) -> int:
    visited = [0] * height * width
    return dfs_recursive(0, starting_col, visited, height, width, lines_list)

def main():
    with open(sys.argv[1]) as file:
        lines_list = file.read().splitlines()
        height = len(lines_list)
        width = len(lines_list[0])

        starting_col = 0
        for i in range(width):
            char = lines_list[0][i]
            if char == "S":
                starting_col = i
        
        ans = dfs(height, width, starting_col, lines_list)
        print(ans)

if __name__ == "__main__":
    main()