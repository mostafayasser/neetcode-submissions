class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seenS = {}
        seenT = {}
        for x in s:
            seenS[x] = seenS.get(x, 0) + 1
        for x in t:
            seenT[x] = seenT.get(x, 0) + 1
        return seenS == seenT
        
        