# coding: utf-8

from typing import List


class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        if digits is None:
            return []
        digits_len = len(digits)
        if digits_len == 0:
            return []

        carry = 1
        digits.reverse()

        for i, digit in enumerate(digits):
            sum_result = digit + carry
            carry = int(sum_result / 10)
            digits[i] = int(sum_result % 10)
        # note: (9 + 1)
        if carry > 0:
            digits.append(carry)

        digits.reverse()
        return digits


if __name__ == "__main__":
    plusOne = Solution()
    origin_list = [0]
    result_list = plusOne.plusOne(digits=origin_list)
    print(result_list)
    origin_list = [9, 9]
    result_list = plusOne.plusOne(digits=origin_list)
    print(result_list)
