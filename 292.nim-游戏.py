#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim 游戏
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        # 1, 2, 3 -> true
        # 4, -> false
        # 5, 6, 7 -> true
        # 8 -> false
        # 9, 10, 11 -> true
        return n & 3
# @lc code=end

