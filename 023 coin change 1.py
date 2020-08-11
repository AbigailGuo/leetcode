
# https://leetcode.com/problems/coin-change/
def change(amount, coins):
    # dp = []
    # for _ in range(0, len(coins)+1):
    #     dp.append([0 for _ in range(0, amount+1)])
    # for i in range(0, len(coins)+1):
    #     dp[i][0] =  1
    # for i in range(1, amount+1):
    #     for j in range(1, len(coins)+1):
    #         if i-coins[j-1]>=0:
    #             dp[j][i] = dp[j][i-coins[j-1]]+ dp[j-1][i]
    #         else:
    #             dp[j][i] = dp[j-1][i]
    # return dp[len(coins)][amount]
    dp = [0 for _ in range(0, amount+1)]
    dp[0] =  1
    for i in  range(0, len(coins)):
        for j in range(1, amount+1): 
            if (j - coins[i] >= 0):
                dp[j] = dp[j] + dp[j-coins[i]]
    return dp[amount]

print(change(5, [1, 2, 5]))
            
        
