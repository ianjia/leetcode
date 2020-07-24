# Merge and Sort
class Solution1(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2) # nums1[:m] (the elements after m are zeroes)

# Two-pointers
class Solution2(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1 # pointer for nums1
        p2 = n - 1 # pointer for nums2
        
        index = m + n - 1 # pointer for both arrays combined
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[index] = nums2[p2]
                p2 -= 1
            else:
                nums1[index] =  nums1[p1]
                p1 -= 1
            index -= 1

        # add the last few parts of p2 to nums1
        nums1[:p2 + 1] = nums2[:p2 + 1]