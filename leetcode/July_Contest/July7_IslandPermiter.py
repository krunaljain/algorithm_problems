class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                water = 0
                if grid[i][j] == 1:
                    if i - 1 < 0 or grid[i - 1][j] == 0:
                        water += 1
                    if i + 1 >= rows or grid[i + 1][j] == 0:
                        water += 1
                    if j - 1 < 0 or grid[i][j - 1] == 0:
                        water += 1
                    if j + 1 >= cols or grid[i][j + 1] == 0:
                        water += 1
                    res += water
        return res