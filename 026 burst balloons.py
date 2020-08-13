# https://leetcode.com/problems/burst-balloons/
def maxCoins(nums):
    points = [1]
    points.extend(nums)
    points.append(1)
    print(points)
    dp = [[0]*(len(nums)+2) for _ in range(len(nums)+2)]
    for i in range(len(nums)+1, -1, -1):
        for j in range(i+1, len(nums)+2):
            res = 0
            for k in range(i+1, j):
                if dp[i][k]+dp[k][j]+points[i]*points[k]*points[j]>res:
                    res = dp[i][k]+dp[k][j]+points[i]*points[k]*points[j]
            dp[i][j] = res
    return dp[0][len(nums)+1]
print(maxCoins([3,1,5,8]))
