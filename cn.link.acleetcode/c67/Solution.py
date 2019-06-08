# coding: utf-8


class Solution:

    def addBinary(self, a: str, b: str) -> str:

        a_len = len(a)
        a = list(a)
        a.reverse()

        b_len = len(b)
        b = list(b)
        b.reverse()

        max_len = max(a_len, b_len)
        # print(max_len)

        result_str = []
        carry = 0
        for i in range(max_len):
            if i < a_len and i < b_len:
                temp = int(a[i]) + int(b[i]) + carry
                carry = int(temp / 2)
                result_str.append(int(temp % 2))
            elif i >= a_len:
                temp = int(b[i]) + carry
                carry = int(temp / 2)
                result_str.append(int(temp % 2))
            elif i >= b_len:
                temp = int(a[i]) + carry
                result_str.append(int(temp % 2))
                carry = int(temp / 2)

        # note: 1 + 1 = 2
        if carry > 0:
            result_str.append(1)
        # print(result_str)
        # result_str.reverse()
        # print(result_str)

        result = ""
        for item in result_str[::-1]:
            result += str(item)

        return result


if __name__ == "__main__":
    solution = Solution()
    a_str = "11"
    b_str = "1"

    result_list = solution.addBinary(a_str, b_str)
    print(result_list)

