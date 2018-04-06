class Solution:
	def reverse(self, x):
		value = ''
        
		if (x < 0):
			value = str(x)[1:]
			value = '-' + str(value)[::-1]
		else:
			value =  str(x)[::-1]

		if (int(value) > 2147483647 or int(value) < -2147483648):
			return 0
		
		return int(value)

x = Solution().reverse(-1534236469)
print(x)