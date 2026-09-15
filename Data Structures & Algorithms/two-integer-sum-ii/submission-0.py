class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        last = len(numbers) - 1
        first = 0
        value = numbers[last] + numbers[first]
        while value != target:
            if value < target:
                first += 1
            else:
                last -= 1
            value = numbers[last] + numbers[first]
        return [first+1, last+1]
