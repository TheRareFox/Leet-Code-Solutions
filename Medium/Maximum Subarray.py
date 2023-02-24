class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        ans = max(nums)
        for num in nums:
            if temp + num > 0:
                temp += num
                ans = temp if ans < temp else ans
            else:
                temp = 0
            
        return ans