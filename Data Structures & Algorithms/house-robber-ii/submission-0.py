class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        else:
            rob_first = nums[0] + self.rob(nums[2:])
            not_first = self.rob(nums[1:])
            return max(rob_first, not_first)