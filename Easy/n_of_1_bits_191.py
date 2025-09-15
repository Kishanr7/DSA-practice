class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_digits = bin(n)[2:]
        print(binary_digits,type(binary_digits))
        return binary_digits.count('1')