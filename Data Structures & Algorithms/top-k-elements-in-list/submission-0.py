class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for n in nums:
            if str(n) in occ:
                occ[str(n)] += 1
            else:
                occ[str(n)] = 1
        most_frequent = sorted(occ.keys(), key=lambda x: occ[str(x)], reverse=True)
        return most_frequent[:k]