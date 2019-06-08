# coding: utf-8


class Solution:
    def countAndSay(self, n: int) -> str:
        res = ["1"]
        for i in range(n):
            num = res[i]
            temp = num[0]
            count = 0
            ans = ""  # 第n+1个数字的结果
            for j in range(0, len(num)):
                if num[j] == temp:
                    count += 1
                else:
                    ans += str(count)
                    ans += str(temp)
                    temp = num[j]
                    count = 1
            ans += str(count)
            ans += str(temp)
            res.append(ans)
        return res[n - 1]


if __name__ == "__main__":
    solution = Solution()
    result = solution.countAndSay(39)
    print(result)
