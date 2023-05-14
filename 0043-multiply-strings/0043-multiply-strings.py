class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        len1, len2 = len(num1), len(num2)
        num1, num2 = num1[::-1], num2[::-1]
        result = [0] * (len1 + len2)
        
        for i in range(len2):
            for j in range(len1):
                digit_prod = int(num2[i]) * int(num1[j])
                result[i + j] += digit_prod % 10
                if result[i + j] >= 10:
                    carry = result[i + j] // 10
                    result[i + j] %= 10
                    result[i + j + 1] += carry
                result[i + j + 1] += digit_prod // 10

        return ''.join([str(x) for x in result[::-1]]).lstrip("0")