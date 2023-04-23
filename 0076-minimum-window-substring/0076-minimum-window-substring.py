from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        left: int = 0
        min_str_len: int = m + 1
        min_str: str = ""
        counter_given: Counter = Counter(t)
        counter_curr: Counter = Counter()
        matched: int = 0

        for right in range(m):
            if s[right] in counter_given:
                counter_curr[s[right]] += 1
                if counter_curr[s[right]] == counter_given[s[right]]:
                    matched += 1

            while matched == len(counter_given):
                if min_str_len > right - left + 1:
                    min_str = s[left : right + 1]
                    min_str_len = right - left + 1
    
                if s[left] in counter_given:
                    counter_curr[s[left]] -= 1
                    if counter_curr[s[left]] == counter_given[s[left]] - 1:
                        matched -= 1
                left += 1

        return min_str
