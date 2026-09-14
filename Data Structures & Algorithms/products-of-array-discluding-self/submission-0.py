class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1 for _ in range(len(nums))]
        
        for n in nums[1:]:
            products[0] *= n

        for i in range(1, len(nums)):
            if nums[i] == 0:
                for n in nums[:i]:
                    products[i] *= n
                if i < len(nums) - 1:
                    for n in nums[i+1:]:
                        products[i] *= n
            else:
                products[i] = products[i-1]*nums[i-1]//nums[i]

        return products
