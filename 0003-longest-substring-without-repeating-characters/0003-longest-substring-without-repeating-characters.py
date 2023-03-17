class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_len: int = 1
        left: int = 0
        right: int = 1
        letters: Set[str] = set(s[0])

        while right < len(s):
            while s[right] in letters:
                letters.remove(s[left])
                left += 1
            letters.add(s[right])
            right += 1
            max_len = max(max_len, len(letters))

        return max_len