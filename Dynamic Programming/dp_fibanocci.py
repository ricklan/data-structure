def dp_fibanocci(num):
    dp = [0] * (num)
    dp[1] = 1
    dp[2] = 1

    for i in range(3, num):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp)


num = 10
dp_fibanocci(num)
