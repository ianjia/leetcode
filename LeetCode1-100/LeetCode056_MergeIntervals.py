# Sorting
class Solution1(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals) # automatically sorts by every subarray's first element
        i = 0
        
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]: # if they are overlapping
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1]) # put merged subarray end time as greatest end time
                intervals.remove(intervals[i+1])
            else:
                i += 1
        
        if len(intervals) > 1: # do final round since the while loop above doesn't merge the second-to-last and last subarrays
            if intervals[-2][1] >= intervals[-1][0]: # if they are overlapping
                intervals[-2][1] = max(intervals[-2][1], intervals[-1][1]) # put merged subarray end time as greatest end time
                intervals.remove(intervals[-1])
                
        return intervals