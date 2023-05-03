from collections import deque
from typing import Deque, Tuple, Set


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count: int = 0

        in_range: Callable[[int, int], int] = lambda idx: 0 <= idx[0] < len(
            grid
        ) and 0 <= idx[1] < len(grid[0])

        dx: List[int] = [-1, 1, 0, 0]
        dy: List[int] = [0, 0, -1, 1]

        visiting: Deque[Tuple[int, int]] = deque()
        visited: Set[Tuple[int, int]] = set()

        def dfs() -> None:
            while visiting:
                curr_row, curr_col = visiting.pop()
                visited.add((curr_row, curr_col))
                for i in range(4):
                    next_row, next_col = curr_row + dx[i], curr_col + dy[i]
                    if (
                        in_range((next_row, next_col))
                        and grid[next_row][next_col] == "1"
                        and (next_row, next_col) not in visited
                    ):
                        visiting.append((next_row, next_col))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    visiting.append((row, col))
                    dfs()
                    count += 1

        return count
