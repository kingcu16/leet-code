#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (39.07%)
# Likes:    952
# Dislikes: 0
# Total Accepted:    101.7K
# Total Submissions: 260.2K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        d = {
            '(':[0,1],
            ')':[0,-1],
            '{':[1,1],
            '}':[1,-1],
            '[':[2,1],
            ']':[2,-1],
        }
        v = []

        for i in s:
            if d[i][1]==1:
                v.append(i)
            else:
                if len(v)==0:
                    return False
                if d[i][0] != d[v.pop()][0]:
                    return False
        if len(v)!=0:
            return False

        return True
