class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len: int = 0
        left: int = 0
        letters: Dict[str, int] = dict()

        for right in range(len(s)):
            if s[right] in letters:
                left = letters[s[right]] + 1 if letters[s[right]] >= left else left
                
            letters[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len