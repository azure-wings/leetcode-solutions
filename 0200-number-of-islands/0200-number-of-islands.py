class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        count: int = 0

        def dfs(row: int, col: int) -> None:
            if grid[row][col] == "1":
                grid[row][col] = "0"
                if row > 0:
                    dfs(row - 1, col)
                if row < num_rows - 1:
                    dfs(row + 1, col)
                if col < num_cols - 1:
                    dfs(row, col + 1)
                if col > 0:
                    dfs(row, col - 1)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)

        return count