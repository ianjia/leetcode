# Sliding Window (two-pointers)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = set() # use set because speed is O(log n) (list speed is O(n))
        slow, fast, curMax = 0, 0, 0
        
        while slow < len(s) and fast < len(s):
            if s[fast] not in visited:
                visited.add(s[fast])
                fast += 1
                curMax = max(curMax, fast - slow)
            else:
                visited.remove(s[slow])
                slow += 1
        return curMax