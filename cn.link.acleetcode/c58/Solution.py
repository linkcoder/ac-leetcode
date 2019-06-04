# coding: utf-8


class Solution:

    # 从后往前找
    def lengthOfLastWord(self, s) -> int:
        """
        :param s:
        :return int:
        """
        s = s.strip()
        str_len = len(s)
        index = str_len-1

        if str_len == 0:
            return 0

        while index >= 0 and s[index] != " ":
            index = index - 1

        return str_len-1 - index


if __name__ == "__main__":
    handler = Solution()
    w_len = handler.lengthOfLastWord("")
    print(w_len)
