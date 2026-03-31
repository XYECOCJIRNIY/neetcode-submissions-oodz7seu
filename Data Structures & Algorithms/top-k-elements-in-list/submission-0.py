class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        for num in nums:
            if num not in s:
                s[num] = 1
            else:
                s[num] += 1
        s2 = list((sorted(s.items(), key=lambda x: x[1], reverse=True)))
        res = []
        for x in s2[:k]:
            res.append(x[0])
        return res