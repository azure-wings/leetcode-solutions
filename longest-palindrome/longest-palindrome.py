class Solution:
    def longestPalindrome(self, s: str) -> int:
        singles = set()
        length = 0

        for c in s:
            if c in singles:
                singles.remove(c)
                length += 2
            else:
                singles.add(c)

        return length + int(len(singles) != 0)