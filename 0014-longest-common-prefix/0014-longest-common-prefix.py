class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix: str = ""

        for letter in zip(*strs):
            if len(set(letter)) == 1:
                prefix += letter[0]
            else:
                break

        return prefix
