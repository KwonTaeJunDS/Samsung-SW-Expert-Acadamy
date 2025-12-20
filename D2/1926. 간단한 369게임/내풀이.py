num = int(input())

def fun(num):
    for i in range(1, num+1):
      # 현재 숫자를 분리 
        lst = list(map(int, str(i)))
        ans = 0

        # 3 6 9 확인하는 구간 
        if lst.count(3):
            ans += lst.count(3)
        if lst.count(6):
            ans += lst.count(6)
        if lst.count(9):
            ans += lst.count(9)

        # 만약 ans가 그대로 0이라면 3,6,9 없는거임 
        if ans != 0:
            print('-'*ans, end=' ')
        else:
            print(i,end=' ')


fun(num)
