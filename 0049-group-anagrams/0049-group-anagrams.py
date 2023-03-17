class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words: DefaultDict[Tuple[str], List[str]] = defaultdict(list)
        for s in strs:
            sorted_words[tuple(sorted(s))].append(s)
        return list(sorted_words.values())