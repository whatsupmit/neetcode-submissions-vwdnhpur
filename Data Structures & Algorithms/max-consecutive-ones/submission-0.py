class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = 0
        count = 0 
        for i in nums:
            if i == 0:
                count = 0
            else:
                count = count + 1
            max_consecutive_ones = max(count, max_consecutive_ones)
        return max_consecutive_ones