class Solution:
	def detectCapitalUse(self, word):

		splitWord = list(word)

		upperCount = 0
		lowerCount = 0

		for x in splitWord:
			if x.isupper():
				upperCount +=1
			else: 
				lowerCount += 1

		if (upperCount == len(word)):
			return True

		elif lowerCount == len(word): 
			return True

		elif splitWord[0].isupper() and lowerCount == len(splitWord) - 1:
			return True
		
		else: 
			return False

x = Solution()
print(x.detectCapitalUse("FlaG"))