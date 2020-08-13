# http://biomaterials.ust.hk/alumni.html
def superEggDrop(K, N):
    # 这个方法超时了
    # 有i个鸡蛋第j层楼,最坏情况要扔几次
    # dp = [[0]*(N+1) for _ in range(K+1)]
    # for i in range(1, N+1):
    #     dp[1][i] = i
    # for i in range(2, K+1):
    #     for j in range(1, N+1):
    #         res = j
    #         for k in range(1, j):
    #             res = min(res, max(dp[i][j-k], dp[i-1][k-1])+1)
    #         dp[i][j] = res


    # return dp[K][N]

    # 根据dp的表的规律发现dp[i][j-k]递减, dp[i-1][k-1]递增, 当两者相等时应该是最优解 
    dp = [[0]*(N+1) for _ in range(K+1)]
    for i in range(1, N+1):
        dp[1][i] = i
    for i in range(2, K+1):
        s = 1
        for j in range(1, N+1):
            dp[i][j] = j
            while s<j and dp[i][j-s]>dp[i-1][s-1]:
                s += 1
            dp[i][j] = min(dp[i][j], max(dp[i][j-s], dp[i-1][s-1])+1)


    return dp[K][N]

    

print(superEggDrop(3, 14))