# -*- coding:utf-8 -*-
class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_map = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in nums_map.keys():
                return [nums_map.get(diff), index]
            nums_map.update({num: index})


def main():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    assert len(result) == 2
    print(result[0], result[1])


main()
