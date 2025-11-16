T = int(input())

for test_case in range(1, T+1):

  num = int(input())

  lst = list(map(int, input().split()))

  count = [0] * 101
  for val in lst:
      count[val] += 1


  fq = max(count)

  for i in range(len(c)):
    if c[i] >= fq:
      fq = c[i]
      ans = i

  print(f'#{num} {ans}')
