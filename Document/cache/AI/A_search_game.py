import heapq

# Direction vectors (up, down, left, right)
dRow = [-1, 1, 0, 0]
dCol = [0, 0, -1, 1]

class Node:
    def __init__(self, row, col, gCost, hCost, parent=None):
        self.row = row
        self.col = col
        self.gCost = gCost
        self.hCost = hCost
        self.parent = parent

    def fCost(self):
        return self.gCost + self.hCost

    def __lt__(self, other):
        return self.fCost() < other.fCost()

def heuristic(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def is_valid(r, c, rows, cols, grid):
    return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0

def print_path(node):
    if not node:
        return
    print_path(node.parent)
    print(f"({node.row},{node.col})", end=" ")

def a_star(grid, start, goal, rows, cols):
    open_set = []
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    sr, sc = start
    gr, gc = goal

    start_node = Node(sr, sc, 0, heuristic(sr, sc, gr, gc))
    heapq.heappush(open_set, start_node)

    while open_set:
        current = heapq.heappop(open_set)

        if visited[current.row][current.col]:
            continue
        visited[current.row][current.col] = True

        if current.row == gr and current.col == gc:
            print("Path found:")
            print_path(current)
            print()
            return True

        for i in range(4):
            newR = current.row + dRow[i]
            newC = current.col + dCol[i]

            if is_valid(newR, newC, rows, cols, grid) and not visited[newR][newC]:
                newG = current.gCost + 1
                newH = heuristic(newR, newC, gr, gc)
                neighbor = Node(newR, newC, newG, newH, current)
                heapq.heappush(open_set, neighbor)

    print("No path found.")
    return False

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    grid = []
    print("Enter grid values (0 = empty, 1 = obstacle):")
    for _ in range(rows):
        grid.append(list(map(int, input().split())))

    sr, sc = map(int, input("Enter start position (row col): ").split())
    gr, gc = map(int, input("Enter goal position (row col): ").split())

    if not is_valid(sr, sc, rows, cols, grid) or not is_valid(gr, gc, rows, cols, grid):
        print("Invalid start or goal position.")
        return

    a_star(grid, (sr, sc), (gr, gc), rows, cols)

if __name__ == "__main__":
    main()
