# Dictionary
class Solution1(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        romanDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        for i in range(0, len(s)):
            num = romanDict[s[i]]
            total += num
            if i >= 1 and romanDict[s[i-1]] < num: # if num's previous is smaller than current num
                smallerRoman = romanDict[s[i-1]]
                total -= 2 * smallerRoman

        return total