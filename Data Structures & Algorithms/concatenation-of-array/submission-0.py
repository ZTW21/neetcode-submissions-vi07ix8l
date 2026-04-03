class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)*2
        l = 0
        r = len(nums)

        while l < len(nums):            
            ans[l] = nums[l]
            ans[r] = nums[l]

            l += 1
            r += 1
        
        return ans