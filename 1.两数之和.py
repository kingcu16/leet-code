#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for i, m in enumerate(nums):
            if _dict.get(target-m) is not None:
                return [_dict.get(target-m), i]
            _dict[m] = i

