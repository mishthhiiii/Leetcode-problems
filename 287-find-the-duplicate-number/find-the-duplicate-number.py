class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            v = abs(nums[i])
            if(nums[v]<0):
                res=v
                break
            else:
                nums[v]*=-1
        for i in range(n):
            if nums[i]<0:
                nums[i]*=-1
        return(res)