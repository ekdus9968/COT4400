"""
COT 4400: Project 1 - Recursive Maze Solver

Team Members:
    -> Seyoung Kan (U36444259)
    -> Kaushik Selvakumar (U75300364)

Brief Description:
    -> This project implements a recursive maze solver using backtracking.
    -> The maze is represented as a 2D grid where 0s represent open paths and 1s represent walls.
    -> The solver starts from a specified position and attempts to find a path to the destination by exploring all possible directions (right, left, down, up).
    -> If a valid path is found, it is printed; otherwise, a message indicating that no path exists is displayed.
"""
# Checking whether move is valid (inside bounds, not wall, not visited)
def isValidMove(maze, x, y, visited):
    n = len(maze)
    return (
        0 <= x < n and
        0 <= y < n and
        maze[x][y] == 0 and
        not visited[x][y]
    )

# Solving maze recursively using backtracking
def solveMaze(maze, x, y, endX, endY, visited, path):

    # Checking if current position reaches destination
    if x == endX and y == endY:
        path.append((x, y))
        return True

    # Stopping recursion if move is invalid
    if not isValidMove(maze, x, y, visited):
        return False

    # Marking current cell as visited
    visited[x][y] = True

    # Adding current cell to path
    path.append((x, y))

    # Exploring right
    if solveMaze(maze, x, y + 1, endX, endY, visited, path):
        return True

    # Exploring left
    if solveMaze(maze, x, y - 1, endX, endY, visited, path):
        return True

    # Exploring down
    if solveMaze(maze, x + 1, y, endX, endY, visited, path):
        return True

    # Exploring up
    if solveMaze(maze, x - 1, y, endX, endY, visited, path):
        return True

    # Backtracking by removing cell from path
    path.pop()

    # Unmarking cell to allow alternate path exploration
    visited[x][y] = False

    return False

# MAZE SOLVER IMPLEMENTATION VALIDATION TEST CASES

# Running one test case and printing output
def runTest(testName, maze, startX, startY, endX, endY):
    print(f"\n--- {testName} ---")

    n = len(maze)
    visited = [[False] * n for _ in range(n)]
    path = []

    if solveMaze(maze, startX, startY, endX, endY, visited, path):
        print("Path Found:")
        print(path)
    else:
        print("No Path Exists")

# Test Case 1 - Valid Path Exists
maze1 = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 0, 0]
]
runTest("Test Case 1 - Valid Path Exists", maze1, 0, 0, 3, 3)

# Test Case 2 - No Possible Path
maze2 = [
    [0, 1, 1],
    [1, 1, 1],
    [1, 1, 0]
]
runTest("Test Case 2 - No Possible Path", maze2, 0, 0, 2, 2)

# Test Case 3 - Start Equals End
maze3 = [
    [0, 1],
    [0, 0]
]
runTest("Test Case 3 - Start Equals End", maze3, 0, 0, 0, 0)

# Test Case 4 - 1x1 Maze
maze4 = [
    [0]
]
runTest("Test Case 4 - 1x1 Maze", maze4, 0, 0, 0, 0)