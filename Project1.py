"""
Team Member: 
Seyoung Kan (U36444259)

< Project1 Recursive Peoblem Solving >
This project focuses only on recursion.
Project 1 must use recursion as the primary solution technique.
Iteration-based solutions are not allowed for this project.

< Project Idea Description >
Given a maze represented as a grid (0 = open path / 1 = wall/blocked path)

Goal :
Find one vaild path from start poisition(0,0) to exit position(3,3) and can move up, down, left, and right only

Recursive Problem :
The maze -solving process natually breaks into smaler subproblems.
Each step attempts to solve a smaller verstion of the maze.

< Analysis >
Time Complexity : O(4^(N^2)) -> Each cell can branch into 4 direstion 
Space Complexity : O(N^2) -> Visited matrix, recursion stack depth 

< Test Case 1 >
Start (0,0)
End (3,3)
Find path from (0,0) to (3,3)

Iuput maze :
0 1 0 0 
0 0 0 1
1 1 0 0 
0 0 0 0 

Output :
[(0,0), (1,0), (1,1), (1,2), (2,2), (3,2), (3,3)]

Edge Cases:
start = end
completely bolcked maze
no possible path
1x1 maze
"""

def is_path(maze, x, y, visited):
    n = len(maze)
    return (0 <= x < n and
            0 <= y < n and
            maze[x][y] == 0 and
            not visited[x][y])
    
def solve_maze(maze, x, y, end_x, end_y, visited, path):
    if x == end_x and y == end_y:
        path.append((x, y))
        return True
    
    if not is_path(maze, x, y, visited):
        return False
    
    visited[x][y] = True
    path.append((x,y))
    
    
    if solve_maze(maze, x, y+1, end_x, end_y, visited, path):
        return True
    
    if solve_maze(maze, x, y-1, end_x, end_y, visited, path):
        return True
    
    if solve_maze(maze, x+1, y, end_x, end_y, visited, path):
        return True
    
    if solve_maze(maze, x - 1, y, end_x, end_y, visited, path):
        return True
    
    path.pop()
    return False

#Testing 
maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0], 
    [0, 0, 0, 0]
]

n = len(maze)
visited = [[False] * n for _ in range(n)]
path =[]

start_x, start_y = 0, 0
end_x, end_y = 3, 3

if solve_maze(maze, start_x, start_y, end_x, end_y, visited, path):
    print("Path Found(Start at(0,0) to End at (3,3)): ")
    print(path)
else: 
    print("No Path Exists")
    
