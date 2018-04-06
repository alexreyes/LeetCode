from string import ascii_lowercase

class Solution(object):
	def isPalindrome(self, s):

		finalList = []
		num = '0123456789'

		
		for char in list(s): 

			if (char.lower() in ascii_lowercase or char.lower() in num):	
				finalList.append(char)

		finalList = ''.join(map(str, finalList))

		if finalList.lower() == finalList[::-1].lower(): return True

		else: return False