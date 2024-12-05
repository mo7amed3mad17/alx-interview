"""
0-island_perimeter
"""
def island_perimeter(grid):
    rows = len(grid)
    columns = len(grid [0])
    perimeter = 0
    coordinates = []

    if rows > 100 or columns > 100:
        return "More Than 100"
    
    for i in range(rows):
        for j in range(columns):
            if grid [i][j] != 0:
                coordinates.append([i, j])

    for (i, j) in coordinates:
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
        if j == columns-1 or grid[i][j+1] == 0:
            perimeter += 1
 
        return perimeter