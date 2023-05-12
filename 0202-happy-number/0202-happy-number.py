class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        visited.add(n)

        def sum_of_digit_square(n: int) -> int:
            output = 0
            while n:
                output += (n % 10) ** 2
                n //= 10

            return output
        
        while n != 1:
            n = sum_of_digit_square(n)
            if n in visited:
                return False
            visited.add(n)
        
        return True