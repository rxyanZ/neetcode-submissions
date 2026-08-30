class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # setup seen map to count which index holds which value
        i = 0
        
        for num in nums:
            find = target - num # value we're looking for to match in nums
            if find in seen:
                return[seen[find], i] # if found in nums we return the current index being referenced and the index of the number were finding that was sent to seen
            seen[num] = i
            i += 1