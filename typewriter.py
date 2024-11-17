class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        ptr = 0
        seconds = 0
        char = 0

        while char < len(word):
            letter = ord(word[char])-97
            if letter == ptr:
                char += 1
                seconds += 1
            elif letter > ptr:
                seconds += 1
                if abs(letter-ptr) > 13:
                    ptr -= 1
                else:
                    ptr += 1
            else:
                seconds += 1
                if abs(letter-ptr) > 13:
                    ptr += 1
                else:
                    ptr -= 1
            if ptr < 0:
                ptr = 25
            if ptr > 25:
                ptr = 0

        return seconds