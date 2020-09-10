# https://leetcode.com/problems/stone-game/
def stoneGame(piles):
    dp = [[[0,0] for _ in range(len(piles))] for _ in range(len(piles))]
    for i in range(len(piles)):
        dp[i][i][0] = piles[i]
    for i in range(len(piles)-1, -1, -1):
        for j in range(i+1, len(piles)):
            left = piles[i]+dp[i+1][j][1]
            right = piles[j]+dp[i][j-1][1]
            if left>right:
                dp[i][j][0] = left
                dp[i][j][1] = dp[i+1][j][0]
            else:
                dp[i][j][0] = right
                dp[i][j][1] = dp[i][j-1][0]
    if dp[0][len(piles)-1][0]>dp[0][len(piles)-1][1]:
        return True
    else:
        return False

print(stoneGame([3,9,1,2]))
