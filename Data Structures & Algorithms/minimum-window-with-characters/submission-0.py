class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s :
            return ""
        required = {}
        for char in t:
            required[char] = required.get(char,0) + 1
        required_count = len(required)
        have =0
        window= {}
        left= 0
        min_len = float('inf')
        start =0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char,0) +1

            if char in required and window[char] == required[char]: have +=1
            while have == required_count:
                if right - left + 1 < min_len:
                    min_len = right - left +1
                    start = left
                
                left_char = s[left]
                window[left_char] -= 1
                if left_char in required and window[left_char] < required[left_char]:
                    have-=1
                left += 1
        return s[start:start + min_len] if min_len != float('inf') else ""
            


