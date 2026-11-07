class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        start = 0
        for i in range(len(nums)):
            if nums[i] is not 0:
                nums[start],nums[i] = nums[i],nums[start]
                start+=1
        