T = int(input())

for test_case in range(1, T + 1):
    
    lst = list(input())

    year = [val for val in lst[:4]]
    year = ''.join(year)

    month = [val for val in lst[4:6]]
    month = ''.join(month)

    day = [val for val in lst[6:8]]
    day = ''.join(day)

    if 0 < int(month) < 13:
        if int(month) in [1,3,5,7,8,10,12]:
            if 0 < int(day) < 32:
                print(f'#{test_case} {year}/{month}/{day}')
            else: 
                print(f'#{test_case} -1')
        elif int(month) in [4, 6,9,11]:
            if 0 < int(day) < 31:
                print(f'#{test_case} {year}/{month}/{day}')
            else: 
                print(f'#{test_case} -1')
        else:
            if 0 < int(day) < 29:
                print(f'#{test_case} {year}/{month}/{day}')
            else: 
                print(f'#{test_case} -1')
    else: 
        print(f'#{test_case} -1')
