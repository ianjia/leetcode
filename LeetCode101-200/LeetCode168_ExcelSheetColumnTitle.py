class Solution1(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # use list instead of dictionary because list already has index
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        result = ""
        
        while n > 0:
            result = letters[(n - 1) % 26] + result # currrent char + result
            n = (n - 1) // 26 # (n - 1) because list starts with index 0, not 1
        
        return result