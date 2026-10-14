class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left, right = 0,0
        longest = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            longest = max(longest, len(window))
        return longest