from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        query: Counter = Counter()
        target: Counter = Counter(p)
        target_len: int = len(p)
        result: List[int] = []
        left: int = 0
        
        for right in range(len(s)):
            query[s[right]] += 1
            if right - left + 1 == target_len:
                if target == query:
                    result.append(left)
                query[s[left]] -= 1
                left += 1

        return result