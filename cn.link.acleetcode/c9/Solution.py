# coding: utf-8

class Solution:

    def isPalindrome(self, x: int) -> bool:
        """
        :param x:
        :return: bool
        """
        x_str = str(x)
        str_len = len(x_str)

        is_pal = True
        for i in range(str_len):
            if x_str[i] == x_str[str_len-i-1]:
                continue
            else:
                is_pal = False
                break
        return is_pal


if __name__ == "__main__":

    solution = Solution()
    print(solution.isPalindrome(1))
