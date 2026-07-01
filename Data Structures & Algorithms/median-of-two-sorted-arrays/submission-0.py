class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []

        i = j = 0
        m,n = len(nums1),len(nums2)

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                res.append(nums2[j])
                j += 1
            else:
                res.append(nums1[i])
                res.append(nums2[j])
                i += 1
                j += 1
        res.extend(nums1[i:])
        res.extend(nums2[j:])
        
        mid = len(res)//2
        median = 0
        if len(res) % 2 == 0:
            median = (res[mid] + res[mid-1])/2
        else:
            median = res[mid]

        return median 