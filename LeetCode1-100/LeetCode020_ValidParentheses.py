# Stack
class Solution1(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for char in s:
            if char in pairs.keys():
                stack.append(char)
                continue
                
            if len(stack) == 0:
                return False
            
            expectedOpeningSymbol = stack.pop()

            if char != pairs[expectedOpeningSymbol]:  # mismatch
                return False
            
        return len(stack) == 0  # false if too many opening symbols