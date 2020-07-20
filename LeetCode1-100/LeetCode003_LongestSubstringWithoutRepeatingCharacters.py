# Sliding Window (two-pointers)
class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = set()
        slow, fast, curMax = 0, 0, 0
        
        while slow < len(s) and fast < len(s):
            if s[fast] not in visited:
                visited.add(s[fast])
                fast += 1
                curMax = max(curMax, fast - slow) # fast - slow (distance between fast and slow)
            else:
                visited.remove(s[slow])
                slow += 1
                
        return curMax