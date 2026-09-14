class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        for n in nums:
            total_prod *= n
        
        products = [total_prod for _ in range(len(nums))]
        
        for i in range(len(nums)):
            if nums[i] == 0:
                products[i] = 1
                for n in nums[:i]:
                    products[i] *= n
                if i < len(nums) - 1:
                    for n in nums[i+1:]:
                        products[i] *= n
            else:
                products[i] = products[i]//nums[i]
        return products
