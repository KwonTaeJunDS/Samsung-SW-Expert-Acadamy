T = int(input())


# 행 방향 
dr = [0, 1, 0, -1]
# 열 방향
dc = [1, 0, -1, 0]
'''
dr, dc = 0, 1 이면 우
1, 0 이면 하
0, -1 이면 좌
-1, 0 이면 상 
'''



for test_case in range(1,T+1):
    n = int(input())

    # 0으로 모두 초기화 
    lst = [[0]*n for i in range(n)]

    # 초기 위치 0,0 정의 
    # r은 행, c는 열을 의미함 
    r, c = 0, 0

    # d(방향)도 초기화
    d = 0

    # n*n 만큼 돌면서 1부터 채워줌
    for num in range(1, n*n+1):

        lst[r][c] = num

        # 새로운 r, c 인덱스 정의 
        nr = r + dr[d]
        nc = c + dc[d]


        # nr, nc가 0보다 작거나 n 보다 커지고 이미 0이 아닌 숫자 (정의가 됨) 라면
        if nr < 0 or nr>=n or nc<0 or nc>=n or lst[nr][nc] !=0:
            # d를 시계 방향으로 회전 
            d = (d+1) % 4
            nr = r+dr[d]
            nc = c+dc[d]
        # r, c 에 갱신 
        r, c = nr, nc

    print(f'#{test_case}')
    for val in lst:
        print(*val)
        
