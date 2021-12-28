//Two sum-https://leetcode.com/problems/two-sum/
//Runtime: 632 ms
//Memory Usage: 14.8 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=[]
        for i in range(len(nums)):
            target=target-nums[i]
            if target in nums[i+1:len(nums)]:
                x.append(i)
                nums[i]=-2
                x.append(nums.index(target))
                break
            else:
                target=target+nums[i]
            
        return x
