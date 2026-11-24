class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = {}
        for str in strs:
            key= "".join(sorted(str)) 
            if key not in strs_map:
                strs_map[key] = []
            strs_map[key].append(str)
        return list(strs_map.values())
        