# Backtracking
class Solution1(object):
    def __init__(self):
        self.result = []
        self.telephoneNums = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return self.result

        curPermute = []

        self.permuteCore(digits, curPermute)
        return self.result

    def permuteCore(self, digits, curPermute):
        if len(digits) == len(curPermute):
            joined = "".join(curPermute)
            self.result.append(joined)
            return
        
        i = len(curPermute)
        chars = self.telephoneNums[digits[i]]
        for j in range(0, len(chars)):   
            curPermute.append(chars[j])
            self.permuteCore(digits, curPermute)
            curPermute.pop()