from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_count = Counter(sorted(words))
        return sorted(words_count, key=words_count.get, reverse=True)[:k]