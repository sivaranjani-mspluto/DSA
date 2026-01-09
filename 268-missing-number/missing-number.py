class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ts,s=0,0
        for i in range(0,len(nums)):
            ts+= i
            s+=nums[i]
        ts+=len(nums)
        return ts-s


