# String
class Solution1(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        res = ""
        i = len(a) - 1
        j = len(b) - 1
        
        while i >= 0 or j >= 0:
            """
            if i >= 0:
                digitA = int(a[i])
            else:
                digitA = 0
            if j >= 0:
                digitB = int(b[j])
            else:
                digitB = 0
            """
            digitA = int(a[i]) if i >= 0 else 0
            digitB = int(b[j]) if j >= 0 else 0
            
            res = str((digitA + digitB + carry) % 2) + res # mod 2 because binary
            carry = (digitA + digitB + carry) // 2
            i -= 1
            j -= 1
            
        if carry == 1: # check one last time
            res = "1" + res
            
        return res

# Built-in Functions
class Solution2(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = int(a, 2), int(b, 2)
        return(bin(a + b)[2:]) # the res needs to be sliced ([2:]) because it somehow returns an extra "0b" in front 