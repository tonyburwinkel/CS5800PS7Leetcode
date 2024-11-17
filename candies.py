class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        total = 0
        sort = sorted(cost)
        while len(sort)>2:
            for i in range(2):
                total+=sort.pop()
            sort.pop()
        while sort:
            total+=sort.pop()

        return total