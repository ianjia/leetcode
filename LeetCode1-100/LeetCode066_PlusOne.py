# Array
class Solution1(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        
        for i in range(len(digits) - 1, -1, -1): # add from the end (normal addition)
            if digits[0] == 10: # if we are down to the last digit and it has a carry
                digits[0] = 0
                digits.insert(0, 1)
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] += 1
            else: # if you don't need to carry, then break
                break
            
        return digits

# Cheat
class Solution2(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        digits = map(str, digits) # convert every element in digits to string
        digits = "".join(digits) # join digits into string
        digits = int(digits) # convert digits (string) into an integer
        digits += 1 # add one to integer
        
        # res appends each element in digits
        for digit in str(digits):
            res.append(digit)
            
        return res