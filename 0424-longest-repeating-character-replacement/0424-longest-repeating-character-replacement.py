from dataclasses import dataclass
from typing import Dict


@dataclass
class LetterCount:
    left: int = 0
    max_len: int = 0
    other_char: int = 0


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters: Dict[str, LetterCount] = {c: LetterCount() for c in s}

        for right in range(len(s)):
            for c in letters:
                if c != s[right]:
                    letters[c].other_char += 1
                    while letters[c].other_char > k:
                        if s[letters[c].left] != c:
                            letters[c].other_char -= 1
                        letters[c].left += 1

                letters[c].max_len = (
                    right - letters[c].left + 1
                    if right - letters[c].left + 1 > letters[c].max_len
                    else letters[c].max_len
                )

        return max(letters[c].max_len for c in letters)
