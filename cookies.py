class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse=True)
        s.sort(reverse=True)
        total = 0
        idx1, idx2 = 0, 0
        while idx1<len(g) and idx2<len(s):
            if g[idx1]<=s[idx2]:
                total+=1
                idx1+=1
                idx2+=1
            else:idx1+=1
        return total