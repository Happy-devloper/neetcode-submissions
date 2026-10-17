class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}
        s2Count = {}
        right = 0
        if len(s1) > len(s2): return False
        for i in range(len(s1)):
            s1Count[s1[i]] =s1Count.get(s1[i],0) +1 
            s2Count[s2[i]] = s2Count.get(s2[i],0) +1
        if s1Count == s2Count : return True
        for right in range(len(s1), len(s2)):

            s2Count[s2[right]] = s2Count.get(s2[right],0)+1
            s2Count[s2[right - len(s1)]] = s2Count.get(s2[right - len(s1)],0)-1
            if s2Count[s2[right - len(s1)]] == 0:
                del s2Count[s2[right - len(s1)]]
            if s2Count == s1Count:
                return True
        return False