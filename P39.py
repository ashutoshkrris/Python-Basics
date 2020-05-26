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
list_nums = list(map(int,input().split(" ")))
tar = int(input())
print(o.twoSum(list_nums,tar))
