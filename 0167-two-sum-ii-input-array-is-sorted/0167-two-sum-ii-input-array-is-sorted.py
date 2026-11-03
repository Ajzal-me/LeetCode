class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while(left<=right):
            
            l= numbers[left]
            r = numbers[right]

            if l + r == target:
                return [left+1,right+1]
            elif l+r<target:
                left = left + 1
            else:
                right = right - 1

        
            
        