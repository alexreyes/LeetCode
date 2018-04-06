class Solution:
    def checkPossibility(self, nums):
        #????
        correctArray = []
        print(nums[-1])
        for x in range(1, nums[-1] + 1):
        	correctArray.append(x)
        
        print(correctArray) 

        # diffCount = 0 

        # for y in range(0, len(nums)): 
        # 	#if (correctArray[y] != nums[x]):
        # 	diffCount += 1

        # print(diffCount)

x = Solution().checkPossibility([1,2,3])