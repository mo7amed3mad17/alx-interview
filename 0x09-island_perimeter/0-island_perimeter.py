#!/usr/bin/python3
"""
island_perimeter file
"""
def island_perimeter(grid):
    """ island_perimeter function"""
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    # List of indices of land cells
    land_indices = [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == 1]
    
    for (i, j) in land_indices:
        # Check up
        if i == 0 or grid[i-1][j] == 0:
            perimeter += 1
        # Check down
        if i == rows-1 or grid[i+1][j] == 0:
            perimeter += 1
        # Check left
        if j == 0 or grid[i][j-1] == 0:
            perimeter += 1
        # Check right
        if j == cols-1 or grid[i][j+1] == 0:
            perimeter += 1
    
    return perimeter
