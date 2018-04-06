class Solution:
    def twoSum(self, nums, target):
    	for i in range(len(nums)):
    		for e in range(len(nums)):
    			if i==e:
    				break
    			else (nums[i] + nums[x]) == target: 
    				return [e,i]

x = Solution().twoSum([3, 3, 11, 15], 6)

print(x)