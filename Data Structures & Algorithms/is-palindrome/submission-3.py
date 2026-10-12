class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = len(s)-1
        y=0
        while y<x:
            if not s[x].isalnum():
                x-=1
                continue
            if not s[y].isalnum():
                y+=1
                continue
            left = s[x].lower()
            right = s[y].lower()
            if left != right: return False
            y +=1
            x -=1
        return True