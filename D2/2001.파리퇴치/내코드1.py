T = int(input())

for test_case in range(1,T+1):

  n, m = map(int, input().split())

  lst = []
  # n x n 행렬 만들기 
  for i in range(n):
    val = list(map(int, input().split()))

    lst.append(val)

# 정답
  max_kill = 0

  # m x m 행렬만큼 n 행렬 돌기 
  for i in range(0, n-m+1):
    for j in range(0, n-m+1):

      hap = 0
      # 누적값 계산 
      for r in range(i, i+m+):
        for c in range(j, j+m):

          hap += lst[r][c]

      # 정답값 갱신 
      max_kill = max(max_kill, hap)

  print(f'#{test_case} {max_kill}'
