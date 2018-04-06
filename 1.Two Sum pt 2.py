class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(0, len(nums)):
        	for x in range(0, len(nums)):
        		if i == x: 
        			break
        		elif (nums[i] + nums[x]) == target:
        			return [x,i]

x = Solution().twoSum([2, 7, 11, 15], 9)
print(x)