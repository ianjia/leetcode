# Vertical scanning
class Solution1(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longestPre = ""
        
        if len(strs) == 0:
            return longestPre
                
        for j in range(0, len(strs[0])):
            curChar = strs[0][j]
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != curChar:
                    return longestPre
            longestPre += curChar
        
        return longestPre