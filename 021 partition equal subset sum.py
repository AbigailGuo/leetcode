def canPartition(nums):
    if sum(nums)%2==1 or not nums:
        return False
    bag = int(sum(nums)/2)
    dp = []
    for i in range(0, len(nums)+1):
        array = []
        for j in range(0, bag+1):
            array.append(False)
        dp.append(array)
    for i in range(0, len(nums)+1):
        dp[i][0] = True
    for i in range(1, len(nums)+1):
        for j in range(1, bag+1):
            if j-nums[i-1]>=0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
        
    for i in range(len(nums)+1):
        if dp[i][bag]:
            return True
    return False



print(canPartition([23,13,11,7,6,5,5]))