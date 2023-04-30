class Solution:
    def longestPalindrome(self, s: str) -> int:
        singles: Set[int] = set()
        palin_len: int = 0

        for c in s:
            if c in singles:
                singles.remove(c)
                palin_len += 2
            else:
                singles.add(c)

        return palin_len + (len(singles) > 0)