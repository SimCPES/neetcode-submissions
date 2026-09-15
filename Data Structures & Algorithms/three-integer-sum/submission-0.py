class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def twoSum(array, target):
            first, last = 0, len(array) - 1
            output = []
            while first < last:
                curSum = array[first] + array[last]
                if curSum == target:
                    output.append((-target, array[first], array[last]))
                    first += 1
                elif curSum < target:
                    first += 1
                else:
                    last -= 1
            return output

        res = set()

        for i, n in enumerate(nums):
            for triple in twoSum(nums[i+1:], -n):
                res.add(triple)

        return [list(triple) for triple in res]
