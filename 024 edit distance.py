# https://leetcode.com/problems/edit-distance/
def minDistance(word1, word2):
    dp = [[float('inf')]*(len(word1)+1) for _ in range(len(word2)+1)]
    for i in range(0, len(word2)+1):
        dp[i][0] =  i
    for j in range(0, len(word1)+1):
        dp[0][j] = j
    for i in range(1, len(word2)+1):
        for j in range(1, len(word1)+1):
            if word1[j-1]==word2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+1)
            print(dp)
    return dp[len(word2)][len(word1)]


print(minDistance("horse", "ros"))
    