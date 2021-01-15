# 38. Ch 04. 코딩테스트 유형별 분석 (동적계획법) - 07.
for _ in range(int(input())):
    k = int(input())
    A = [0] + list(map(int, input().split()))
    # S[i]는 1번부터 i번까지의 누적합
    S = [0 for _ in range(k+1)]
    for i in range(1, k+1):
        S[i] = S[i-1] + A[i]
    DP = [[0]*(k+1) for _ in range(k+1)]
    for i in range(2, k+1): # 부분파일의 길이
        for j in range(1, k)
    # dp[i][j] : i에서 j까지 합하는데 필요한 최소비용
    # dp[i][k] + dp[k+1][j] + sum(A[i]~A[j])
    