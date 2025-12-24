num = int(input())

# 3*3 박스 범위
box_lst = [(0, 0), (0,3), (0,6),
           (3, 0), (3,3), (3,6),
           (6, 0), (6, 3), (6,6)]

for test_case in range(1, num+1):

    lst = []

    for i in range(9):
        nlst = list(map(int, input().split()))
        lst.append(nlst)

    ans = 1

    # 행 부분 확인 
    for i in range(len(lst)):
        if len(set(lst[i])) != 9:
            ans = 0
            break

    # 열 부분 확인
    for i in range(len(lst)):
        col_lst = []
        for j in range(9):
            # 열 부분의 값을 모아야 하니 
            col_lst.append(lst[j][i])
        
        if len(set(col_lst)) != 9:
            ans = 0
            break

    # 박스 돌면서 확인 
    for r, c in box_lst:
        new_box = []
        for i in range(r, r+3):
            for j in range(c, c+3):
                new_box.append(lst[i][j])

        if len(set(new_box)) != 9:
            ans = 0
            break


    print(f'#{test_case} {ans}')
        



