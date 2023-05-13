class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ball_redirect = {
            ("down", 1): "right",
            ("down", -1): "left",
            ("left", 1): "stuck",
            ("left", -1): "down",
            ("right", 1): "down",
            ("right", -1): "stuck",
        }
        
        def ball_next_pos(row: int, col: int, direction: str) -> Tuple[int, int]:
            if direction == "down":
                return (row + 1, col)
            elif direction == "left":
                return (row, col - 1)
            elif direction == "right":
                return (row, col + 1)

        final_row = len(grid)
        final_col = len(grid[0])
        result = []
        
        for i in range(final_col):
            curr_dir = "down"
            ball_row, ball_col = 0, i

            while True:
                curr_dir = ball_redirect[(curr_dir, grid[ball_row][ball_col])]
                if curr_dir == "stuck":
                    result.append(-1)
                    break
                ball_row, ball_col = ball_next_pos(ball_row, ball_col, curr_dir)
                if ball_row == final_row:
                    result.append(ball_col)
                    break
                elif not (0 <= ball_col < final_col):
                    result.append(-1)
                    break

        return result