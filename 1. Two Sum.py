class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i

        for i in range(len(nums)):
            next_pair = target - nums[i]
            if next_pair in h and h[next_pair] != i:
                return [ i, h[next_pair] ]