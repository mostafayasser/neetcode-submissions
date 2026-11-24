class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res = ""
        for x in strs:
            res += str(len(x)) + "#" + x
        return res



    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        res = []
        i = 0
        while i != -1:
            y = s.find("#", i)
            l = int(s[i:y])
            new_i = y+1
            if l > 0:
                res.append(s[new_i:new_i+l])
            else:
                res.append("")
            if(new_i+l >= len(s)):
                    i = -1
            else:
                    i = new_i + l
        return res

        
