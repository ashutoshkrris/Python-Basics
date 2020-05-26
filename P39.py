#python 3.7.1 by Ashutosh Krishna

class Solution(object):
   def twoSum(self, nums, target):
       dict = {}
       for i in range(len(nums)):
         if nums[i] in dict:
           return (dict[nums[i]],i)
         else:
           dict[target-nums[i]] = i
           
o = Solution()
print(o.twoSum([2,7,11,15],9))