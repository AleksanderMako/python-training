class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sums ={}
        sum =0 
        sums[0]=1
        frequency =0
        for _,n in enumerate(nums):
            sum+=n
            if (sum-k) in sums: frequency +=sums[sum-k]
            if sum in sums: sums[sum]+=1
            else: sums[sum] =1
        return frequency

