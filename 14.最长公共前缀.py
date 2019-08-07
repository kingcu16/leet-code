#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.28%)
# Likes:    633
# Dislikes: 0
# Total Accepted:    103.3K
# Total Submissions: 301.3K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # min_ = len(strs[0])
        if len(strs)==1:
            return strs[0]
        if len(strs)==0:
            return ""

        s = strs[0]
        index = len(s)
        for ss in strs[1:]:
            if len(ss) < index:
                index = len(ss)
            f = -1
            for i in range(index, 0, -1):
                if s[i-1] != ss[i-1]:
                    f = i
            if f==1:
                return ""

            if f > 0:
                index = f-1

        return s[:index] 

