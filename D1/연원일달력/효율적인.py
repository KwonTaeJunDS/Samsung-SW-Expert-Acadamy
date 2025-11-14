T = int(input())

# 미리 다 정의 
days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

for test_case in range(1, T + 1):
    lst = input().strip()
    
    
    year = lst[:4]
    month = int(lst[4:6])
    day = int(lst[6:8])

    ans = -1

    # 두 조건을 모두 확인 
    if 1 <= month <= 12 and 1 <= day <= days_in_month[month]:
        ans = f'{year}/{lst[4:6]}/{lst[6:8]}'


    print(f'#{test_case} {ans}')
