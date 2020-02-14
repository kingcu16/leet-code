#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (43.95%)
# Likes:    292
# Dislikes: 0
# Total Accepted:    61.4K
# Total Submissions: 139.6K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
# 你可以假设数组中无重复元素。
# 
# 示例 1:
# 
# 输入: [1,3,5,6], 5
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [1,3,5,6], 2
# 输出: 1
# 
# 
# 示例 3:
# 
# 输入: [1,3,5,6], 7
# 输出: 4
# 
# 
# 示例 4:
# 
# 输入: [1,3,5,6], 0
# 输出: 0
# 
# 
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] >= target:
                return 0
            return 1
        
        if target <= nums[0]:
            return 0
        
        if target == nums[-1]:
            return len(nums)-1
        
        if target > nums[-1]:
            return len(nums)
        
        if len(nums) == 2:
            return 1
        
        l = 0
        r = len(nums)-1
        m = (l+r) // 2

        while True:
            if target == nums[m]:
                return m
            
            if target < nums[m]:
                if target == nums[l]:
                    return l
                r = m
                m = (l + r) // 2

                if m == l:
                    return r
            
                continue
            
            if target > nums[m]:
                if target == nums[r]:
                    return r
                
                l = m
                m = (l+r) // 2

                if m == l:
                    return r
                



