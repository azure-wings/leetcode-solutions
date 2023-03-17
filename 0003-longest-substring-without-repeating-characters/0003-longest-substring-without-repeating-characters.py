class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_len: int = 1
        left: int = 0
        right: int = 1
        letters: Dict[str, int] = {s[left]: left}

        while right < len(s):
            if s[right] in letters:
                left = letters[s[right]] + 1 if letters[s[right]] >= left else left
                
            letters[s[right]] = right
            right += 1
            max_len = max(max_len, right - left)

        return max_len