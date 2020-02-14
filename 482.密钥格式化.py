#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        new_str = ''
        sub_idx = 0
        for s in S[::-1]:
            if s == '-':
                continue
            if sub_idx == K:
                new_str += '-'
                sub_idx = 0
            if s.isalpha():
                new_str += s.upper()
                sub_idx += 1
            else:
                new_str += s
                sub_idx += 1
        return new_str[::-1]
# @lc code=end

