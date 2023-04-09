from collections import defaultdict
from typing import DefaultDict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left: int = 0
        counts: DefaultDict[str, int] = defaultdict(int)
        max_len: int = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            curr_len: int = right - left + 1
            if curr_len - max(counts.values()) <= k:
                max_len = (
                    curr_len if curr_len > max_len
                    else max_len
                )
            else:
                counts[s[left]] -= 1
                left += 1

        return max_len
