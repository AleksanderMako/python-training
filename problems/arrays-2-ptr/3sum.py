class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sums =[]
        for i in range(len(nums)):
            if nums[i] >0:
                break
            if i ==0 or nums[i] != nums[i-1]:
              self.twoSum(i,nums,sums)
        return sums

    def twoSum(self,  i: int, nums: List[int],result:List[List[int]]):
        l = i+1
        r = len(nums)-1

        
        while l < r:
            sum = nums[i]+nums[l]+nums[r]
            if sum < 0 or (l >i+1 and nums[l] == nums[l-1]):
                l+=1
            elif sum >0 or (r < len(nums) -1 and nums[r]==nums[r+1]):
                r-=1
            else :
                result.append([nums[i],nums[l],nums[r]])
                l+=1
                r-=1
        
