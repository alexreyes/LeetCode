class Solution:
	def fizzBuzz(self, n):
		arr = []

		for i in range(1, n + 1): 
			if (i % 5 == 0 and i % 3 == 0):
				arr.append("FizzBuzz")
			elif (i % 3 == 0):
				arr.append("Fizz")
			elif (i % 5 == 0):
				arr.append("Buzz")
			else: 
				arr.append("" + i)
		return arr

x = Solution().fizzBuzz(15)
print(x)