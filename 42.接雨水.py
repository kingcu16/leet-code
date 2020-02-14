#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def calcJustOne(self, bh:list) -> int:
        if len(bh) <= 2:
            return 0
            
        h1 = bh[0]
        s = 0
        for hh in bh[1:-1]:
            s += h1 - hh
        return s

    def trap(self, height: list) -> int:
        if len(height) <= 2:
            return 0
        s = 0
        pre = height[0]
        nn = [pre]
        for h in height[1:]:
            if h >= pre:
                nn.append(h)
                pre = h
                s += self.calcJustOne(nn)
                nn = [pre]
            else:
                nn.append(h)
        s += self.trap(nn[::-1])
        return s

if __name__ == '__main__':
    s = Solution()
    s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
# @lc code=end

