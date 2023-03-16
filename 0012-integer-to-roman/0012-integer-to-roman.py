class Solution:
    def intToRoman(self, num: int) -> str:
        roman: str = ""
        digits: List[int] = [1000, 100, 10, 1]
        romans: Dict[int, str] = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        
        for digit in digits:
            while (curr := num // digit):
                if curr in {4, 5, 9}:
                    roman += romans[curr*digit]
                    num -= curr*digit
                elif curr > 5:
                    roman += romans[5*digit]
                    num -= 5*digit
                else:
                    for _ in range(curr):
                        roman += romans[digit]
                        num -= digit
                        
        return roman