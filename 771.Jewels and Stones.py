class Solution:
    def numJewelsInStones(self, J, S):

        count = 0

        splitJ = list(J)
        splitS = list(S)

        for x in S: 
        	for y in J: 
        		if y == x:
        			count += 1

        return count