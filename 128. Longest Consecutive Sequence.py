class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)    #using hashset
        max_count = 0

        for number in nums:
            count = 1
            if number-1 not in nums:    #if "number" is the first element of the sequence
                while number+1 in nums: #loop until the sequence breaks
                    number = number+1
                    count+=1

            max_count = max(count, max_count)
        return max_count