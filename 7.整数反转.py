#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
class Solution:
    def reverse(self, x: int) -> int:
        t = str(abs(x))
        t_ = int(t[::-1], base=10)
        t_ = t_ if x >0 else -t_
        if t_ < -2**31 or t_ > 2**31 -1:
            return 0
        return t_

