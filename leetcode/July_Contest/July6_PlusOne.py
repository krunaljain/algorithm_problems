class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i], carry = (digits[i] + carry) % 10, (digits[i] + carry) // 10
            if carry == 0:
                break
        if carry == 1:
            digits[0]: digits[1:] = carry, digits
        return digits
