class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        least = float('inf')
        while left <= right:
            mid = (left+right)//2

            if nums[mid] > nums[right]:
                left = mid +1
                least = min(least,nums[mid])
            else:
                right = mid -1
                least = min(least,nums[mid])
        return least

