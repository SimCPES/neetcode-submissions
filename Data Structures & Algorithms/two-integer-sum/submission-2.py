class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums[:-1]):
            if target - n in nums[i+1:]:
                complement = nums[i+1:].index(target - n)
                return [i, complement+i+1]