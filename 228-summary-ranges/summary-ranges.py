class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i,j=0,0
        res=[]
        while j<len(nums) and i<len(nums):
            if j < len(nums)-1 and (nums[j+1] == nums[j]+1):
                j+=1
            else :
                if nums[i] == nums[j]:
                    res.append(str(nums[i]))
                else:
                    res.append(str(nums[i])+"->"+str(nums[j]))
                i,j=j+1,j+1
        return res