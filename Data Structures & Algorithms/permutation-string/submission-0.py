class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        s2_count = {}
        right, left = 0,0
        for i in s1:
            s1_count[i] = s1_count.get(i,0)+1
        for right in range(len(s2)):
            s2_count[s2[right]] = s2_count.get(s2[right],0)+1
            if (right - left+1)>len(s1):
                s2_count[s2[left]] -= 1
                if s2_count[s2[left]]==0:
                    del s2_count[s2[left]]
                left +=1
            if s2_count == s1_count:
                return True
        return False