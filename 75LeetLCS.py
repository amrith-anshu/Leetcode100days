#Longest Common Subsequence between text1 and text2.
#technique used 2d grid and updating value by bottom up Dynamic programming.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        #intialised 0 to all indexes of 2d grid.

        for i in range(len(text1) -1,-1,-1):
            for j in range(len(text2) -1,-1,-1):
                #for checking the value in 2d grid
                if text1[i] == text2[j]:
                    dp[i][j]=1+dp[i+1][j+1] #adds+1 to diagonal value and stores in it.
                    #if both row and colunmn are equal,add+1 to cross index in the grid.
                else:
                    dp[i][j]=max(dp[i][j+1],dp[i+1][j])
                    #if not equal, then check the max value between bottom and right index val
        return dp[0][0]
        #the starting index will be updated and will be the result.
