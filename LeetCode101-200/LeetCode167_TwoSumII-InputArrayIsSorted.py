# Two-pointers
class Solution1(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers) - 1
        
        # two pointers move inward (towards the middle)
        while numbers[start] + numbers[end] != target:
            if numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1
        return [start + 1, end + 1]