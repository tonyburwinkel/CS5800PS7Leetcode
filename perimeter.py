class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort = sorted(nums)
        for i in range(len(sort)-1, 1, -1):
            if sort[i-1] + sort[i-2] > sort[i]:
                return sort[i] + sort[i-1]+ sort[i-2]
        return 0