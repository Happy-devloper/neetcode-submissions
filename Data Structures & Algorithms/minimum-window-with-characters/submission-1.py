class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        window = {}
        right,left = 0,0
        have = 0
        min_len = float('inf')
        start = 0
        if len(s)< len(t) : return ""
        for i in range(len(t)):
            t_count[t[i]] = t_count.get(t[i],0) +1
        required = len(t_count)

        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0)+1
            if s[right] in t_count and window[s[right]] == t_count[s[right]]:
                have +=1
            while have == required:
                if right- left +1 < min_len:
                    min_len = right -left+1
                    start = left
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]: have -= 1
                left +=1
        return s[start:start +min_len] if min_len != float('inf') else ""