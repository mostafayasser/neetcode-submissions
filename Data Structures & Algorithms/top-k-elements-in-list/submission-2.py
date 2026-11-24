class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)
        freq = [[] for i in range(len(nums)+ 1)  ]
        for n,c in freq_map.items():
            freq[c].append(n)
        res = []
        while len(res) < k:
            res.extend(freq.pop())
        return res