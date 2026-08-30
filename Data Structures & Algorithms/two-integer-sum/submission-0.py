class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #setup 
        i = 0
        
        for num in nums:
            find = target - num
            if find in seen:
                return[seen[find], i]
            seen[num] = i
            i += 1