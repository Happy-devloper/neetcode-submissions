class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        all= []
        for i in nums1:
            all.append(i)
        for j in nums2:
            all.append(j)
        all.sort()
        right = len(all)-1
        mid = right //2
        if right % 2 == 0:
            return float(all[mid])
        else:
            median = (all[mid]+all[mid+1])/2
            return median