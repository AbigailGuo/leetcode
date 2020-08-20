# https://leetcode.com/problems/longest-common-subsequence/
def longestCommonSubsequence(text1, text2):
    dp = [[0]*(len(text1)+1) for _ in range(len(text2)+1)]
    for i in range(1, len(text2)+1):
            for j in range(1, len(text1)+1):
                if text1[j-1]==text2[i-1]:
                    dp[i][j] += dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len(text2)][len(text1)]

print(longestCommonSubsequence("bsbininm"
,"jmjkbkjkv"))