class Solution:
	def romanToInt(self, s):

		one = "I"
		five = "V"
		ten = "X"
		fifty = "L"
		hundred = "C"
		fiveHundred = "D"
		thousand = "M"

		splitString = list(s)
		toInt = 0

		for i in splitString:
			if (i == one):
				toInt += 1
			elif (i == five):
				toInt +=5
			elif (i == ten): 
				toInt += 10
			elif (i == fifty): 
				toInt += 50
			elif (i == hundred): 
				toInt += 100
			elif (i == fiveHundred): 
				toInt += 500
			elif (i == thousand): 
				toInt += 1000
		
		return toInt

x = Solution().romanToInt("MMXVII")
print(x)