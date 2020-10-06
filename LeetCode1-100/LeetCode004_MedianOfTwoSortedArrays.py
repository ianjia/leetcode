# O(n log n)
class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        mid = len(nums1) // 2
        if len(nums1) % 2 != 0:
            return nums1[mid]
        else:
            return (nums1[mid] + nums1[mid-1]) / 2 # Only works in Python 3 because "/ 2" in Python will not give a float

# O(n)
class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        nums1.extend([0] * n)
        self.merge(nums1, m, nums2, n)
        mid = len(nums1) // 2
        if len(nums1) % 2 != 0:
            return nums1[mid]
        else:
            return (nums1[mid] + nums1[mid-1]) / 2
        
    def merge(self, nums1, m, nums2, n):
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
        
# Binary Search - O(log min(n, m))
class Solution3:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
            
        imin, imax, halfLen = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = halfLen - i
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0: maxl = nums2[j-1]
                elif j == 0: maxl = nums1[i-1]
                else: maxl = max(nums1[i-1], nums2[j-1])
                if (m+n) & 1:
                    return maxl
                if i == m: minr = nums2[j]
                elif j == n: minr = nums1[i]
                else: minr = min(nums1[i], nums2[j])
                return (maxl + minr) / 2.0