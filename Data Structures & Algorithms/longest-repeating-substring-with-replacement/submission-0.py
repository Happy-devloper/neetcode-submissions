class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        right,left = 0,0
        longest = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0) +1
            while (right - left +1) - max(count.values()) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left +=1
            longest = max(right -left +1,longest)
        return longest
            