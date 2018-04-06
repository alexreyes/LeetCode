from string import ascii_lowercase

class Solution:
	def uniqueMorseRepresentations(self, words):

		morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
		convertedWord = []
		megaList = []

		for word in words: 

			for letter in list(word):

				convertedWord.append(morseCode[ascii_lowercase.index(letter)])
			
			megaList.append(''.join(convertedWord))
			convertedWord = []

		return len(list(set(megaList)))