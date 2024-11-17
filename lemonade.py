class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fives = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                fives+=1
            if bill == 10:
                tens+=1
            change = bill - 5
            if change == 0:
                continue
            while change >=10 and tens > 0:
                change -=10
                tens -= 1
            while change >= 5 and fives > 0:
                change -= 5
                fives -= 1
            if change != 0:
                return False
        return True