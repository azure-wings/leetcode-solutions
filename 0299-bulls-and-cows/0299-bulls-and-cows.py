from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls: int = 0
        cows: int = 0
        secret_counter: Counter = Counter(secret)
        guess_counter: Counter = Counter(guess)
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1

        cows = sum((secret_counter & guess_counter).values()) - bulls

        return f"{bulls}A{cows}B"