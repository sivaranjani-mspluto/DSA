class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=1
        r=1
        n=len(nums)
        larr=[0]*n
        rarr=[0]*n
        for i in range(n):
            j= -i-1
            larr[i]=l
            rarr[j]=r
            l*=nums[i]
            r*=nums[j]
        return [l*r for l,r in zip(larr,rarr)]
