class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            nums.pop()
            if n in nums:
                return True
        return False
            

        