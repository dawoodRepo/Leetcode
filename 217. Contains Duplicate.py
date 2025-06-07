class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # using hash set
        check = set()
        for num in nums:
            if num in check:
                return True
            else:
                check.add(num)
        return False