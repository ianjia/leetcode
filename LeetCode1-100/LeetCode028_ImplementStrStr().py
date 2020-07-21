# Slice
class Solution1(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lenHaystack = len(haystack)
        lenNeedle = len(needle)
        
        if needle not in haystack:
            return -1
        
        if needle == "" or lenHaystack == lenNeedle: # lenHaystack == lenNeedle (the haystack is the needle)
            return 0
        
        for i in range(0, lenHaystack - lenNeedle + 1):
            if haystack[i:lenNeedle + i] == needle:
                return i