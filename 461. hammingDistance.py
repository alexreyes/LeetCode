class Solution:
	def hammingDistance(self, x, y):
		
		binX = str(bin(x)).replace('b', '0')
		binY = str(bin(y)).replace('b', '0')

		if (len(binX) < len(binY)):
			#Get the number of additional zeroes needed
			additionalZeroes = '0' * (len(binY) - len(binX) )

			binX = additionalZeroes + binX
		
		elif (len(binY) < len(binX)):
			additionalZeroesY = '0' * (len(binX) - len(binY) )

			binY = additionalZeroesY + binY
		
		diffCount = 0
		binX = list(binX)
		binY = list(binY)
		
		count = 0

		for i in binX:
			if (binX[count] != binY[count]):
				diffCount += 1
			count += 1

		return diffCount

x = Solution().hammingDistance(1,64)
print(x)