n = int(input())

for i in range(1, n + 1):
    # 문자열로 변경 
    s = str(i)
    # 한번에 다 확인 
    clap = s.count("3") + s.count("6") + s.count("9")
   # print문도 한줄로 
    print("-" * clap if clap else i, end=" ")
