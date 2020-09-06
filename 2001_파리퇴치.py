t = int(input())
for n in range(1, t+1):
    N, M = map(int, input().split()) #영역크기랑 파리채크기 받아옴
    spaceList = list()  #영역 크기 리스트
    for _ in range(N):
        spaceList.append(list(map(int, input().split()))) #영역 리스트
    sumRows, maxSum = 0, 0
    for r in range(N - M + 1): #기준이 되는 행 번호
        for c in range(N - M +1): #기준이 되는 열 번호
            for m in range(M):
                for mm in range(M):
                    sumRows += spaceList[r+m][c+mm]
            if maxSum < sumRows:
                maxSum = sumRows
            sumRows = 0
    print("#{} {}".format(n, maxSum))