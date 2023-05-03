from collections import deque
from typing import Deque, Tuple, Set


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        in_range: Callable[[int, int], int] = \
            lambda idx: 0 <= idx[0] < len(image) \
            and 0 <= idx[1] < len(image[0])

        dx: List[int] = [-1, 1, 0, 0]
        dy: List[int] = [0, 0, -1, 1]

        visiting: Deque[Tuple[int, int]] = deque()
        visited: Set[Tuple[int, int]] = set()
        visiting.append((sr, sc))
        init_color: int = image[sr][sc]

        while visiting:
            curr_row, curr_col = visiting.pop()
            if (curr_row, curr_col) not in visited:
                visited.add((curr_row, curr_col))
                image[curr_row][curr_col] = color
                for i in range(4):
                    next_row, next_col = curr_row + dx[i], curr_col + dy[i]
                    if (
                        in_range((next_row, next_col))
                        and image[next_row][next_col] == init_color
                    ):
                        visiting.append((next_row, next_col))

        return image
