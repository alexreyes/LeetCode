class Solution:
	def findWords(self, words):
		rows = [['qwertyuiop'],['asdfghjkl'],['zxcvbnm']]

		output = []

		for w in words:

			rowCount = [0,0,0]

			for count in range(0,len(w)):

				if(w[count].lower() in list(rows[0][0])):
					rowCount[0] += 1

				if (w[count].lower() in list(rows[1][0])):
					rowCount[1] += 1

				if (w[count].lower() in list(rows[2][0])):
					rowCount[2] += 1

			if rowCount[0] == len(w) or rowCount[1] == len(w) or rowCount[2] == len(w):
				output.append(w)

		return output
x = Solution().findWords(["qwerty","asdf", "Alaska", "Dad", "Peace"])
print(x)