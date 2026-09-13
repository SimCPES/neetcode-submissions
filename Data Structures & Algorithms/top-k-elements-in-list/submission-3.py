class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for n in nums:
            if str(n) in occ:
                occ[str(n)] += 1
            else:
                occ[str(n)] = 1 
        frequency = [[] for _ in range(len(nums))]
        for n in occ:
            frequency[occ[n] - 1].append(int(n))
        most_frequent = []
        for i in range(len(frequency), 0, -1):
            if len(frequency[i-1]) > 0:
                most_frequent.extend(frequency[i-1])
            if len(most_frequent) >= k:
                return most_frequent[:k]