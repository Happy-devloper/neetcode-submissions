class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right
        while left <= right:
            k = (left+right) //2
            time = 0
            for i in range(len(piles)):
                time = time +math.ceil(piles[i]/k)
            if time > h:
                left = k +1
            else:
                result = k
                right = k-1

        return result