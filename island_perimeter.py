'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
 Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
  and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
 One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]] => 3 + 3 + 0 + 3 +2 + 3 + 2 = 16

'''
def islandPerimeter(grid):
    r = len(grid)
    c = len(grid[0])
    perimeter = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                unit = 4
                if i - 1 >= 0 and grid[i-1][j] == 1:
                    unit -= 1
                if i + 1 < r and grid[i+1][j] == 1:
                    unit -= 1
                if j - 1 >= 0 and grid[i][j-1] == 1:
                    unit -= 1
                if j + 1 < c and grid[i][j+1] == 1:
                    unit -=1
                perimeter += unit
    return perimeter


grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

print islandPerimeter(grid)