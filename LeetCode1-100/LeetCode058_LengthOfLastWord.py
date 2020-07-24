# Built-in String Functions
class Solution1(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.strip() == "":
            return 0
        
        intoList = s.split()
        
        return len(intoList[-1])