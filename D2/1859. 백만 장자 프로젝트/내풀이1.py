T = int(input())

for test_case in range(1, T+1):

  num = int(input())
  lst = list(map(int, input().split()))

  ans, mx= 0, 0

 # 거꾸로 돌면서 확인하면 쉽게 풀이 가능 
  for i in range(num-1, -1, -1):
    if i == num-1:
      mx = lst[i]


    if lst[i] < mx:
      ans += (mx-lst[i])
    else:
      mx = lst[i]

print(f'#{test_case} {ans}')
    
