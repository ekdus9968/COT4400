"""
Team Member: 
Seyoung Kan (U36444259)
Kaushik Selvakumar (U75300364)
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
    
