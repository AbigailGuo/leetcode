def findTargetSumWays(nums, S):
    if (sum(nums)+S)%2 == 1 or sum(nums)<S:
        return 0
    count = 0
    bag = int((sum(nums)+S)/2)
    sum_A = 0
    dp = []
    array = [1]
    for j in range(1, bag+1):
        array.append(0)
    dp.append(array)
    for i in range(1, len(nums)+1):
        array = [1]
        for j in range(1, bag+1):
            array.append(0)
        dp.append(array)
    # print(dp)
    for i in range(1, len(nums)+1):
        for j in range(0, bag+1):
            if j-nums[i-1]>=0:
                dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    return dp[len(nums)][bag]

print(findTargetSumWays([0,0,0,0,0,0,0,0,1], 1))