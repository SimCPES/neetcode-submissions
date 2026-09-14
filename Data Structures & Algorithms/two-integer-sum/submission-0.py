class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            if target - n in nums:
                complement = nums.index(target - n)
                return [i, complement]