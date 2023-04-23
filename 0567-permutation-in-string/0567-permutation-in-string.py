from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_given: Counter = Counter(s1)
        counter_curr: Counter = Counter()
        l1, l2, lt = len(s1), len(s2), len(counter_given)
        matched: int = 0

        for right in range(l2):
            if s2[right] in counter_given:
                counter_curr[s2[right]] += 1
                if counter_curr[s2[right]] == counter_given[s2[right]]:
                    matched += 1

            left = right - l1

            if left >= 0 and s2[left] in counter_given:
                if counter_curr[s2[left]] == counter_given[s2[left]]:
                    matched -= 1
                counter_curr[s2[left]] -= 1

            if matched == lt:
                return True

        return False