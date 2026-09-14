class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_first = nums[:-1]
        nums_last = nums[1:]
        
        def dfs(nums_list: List[int], i: int, seen: List[int]) -> int:
            if len(nums_list) - i <= 3:
                seen[i] = max(nums_list[i:])
                return seen[i]
            else:
                if seen[i+2] == -1:
                    seen[i+2] = dfs(nums_list, i+2, seen)
                if seen[i+1] == -1:
                    seen[i+1] = dfs(nums_list, i+1, seen)
                seen[i] = max(nums_list[i] + seen[i+2], seen[i+1])
                return seen[i]

        seen = [-1 for _ in range(len(nums))]
        max_first = dfs(nums_first, 0, seen)
        seen = [-1 for _ in range(len(nums))]
        max_last = dfs(nums_last, 0, seen)
        return max(max_first, max_last)