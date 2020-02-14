#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        m = []
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1 + l2
        m1, m2 = 0, 0
        if l % 2 == 0:
            m1 = l / 2 - 1
            m2 = l / 2
        else:
            m1 = (l - 1) / 2
            m2 = m1
        idx = 0
        mid = 0
        idx1 = 0
        idx2 = 0
        for i in range(l):
            t = 0
            if idx1 == l1 or idx2 == l2:
                if idx1 == l1:
                    t = nums2[idx2]
                    if i == m1:
                        mid += t
                    if i == m2:
                        mid += t
                        return mid / 2.0
                    idx2 += 1
                else:
                    t= nums1[idx1]
                    if i == m1:
                        mid += t
                    if i == m2:
                        mid += t
                        return mid / 2.0
                    idx1 += 1
            else:
                if nums1[idx1] > nums2[idx2]:
                    t = nums2[idx2]
                    idx2 = idx2 + 1
                    if i == m1:
                        mid += t
                    if i == m2:
                        mid += t
                        return mid / 2.0
                elif nums1[idx1] <= nums2[idx2]:
                    t = nums1[idx1]
                    idx1 += 1
                    if i == m1:
                        mid += t
                    if i == m2:
                        mid += t
                        return mid / 2.0
                
# if __name__ == '__main__':
#     s = Solution()
#     print(s.findMedianSortedArrays([1,3], [2]))
# @lc code=end

