t = int(input())
for i in range(1, t+1):
    N, K = map(int, input().split())
    wordMat = list()
    for _ in range(N):
        wordMat.append(list(map(int, input().split())))

    total = 0
    for r in range(N):
        sumRow = 0
        for c in range(N):
            rowNum = wordMat[r][c]
            if rowNum == 1:
                sumRow += 1
            elif rowNum == 0:
                if sumRow == K:
                    total += 1
                sumRow = 0
        #끝까지 1일 경우 처리
        if sumRow == K:
            total += 1

    for r in range(N):
        sumCol = 0
        for c in range(N):
            colNum = wordMat[c][r]
            if colNum == 1:
                sumCol += 1
            elif colNum == 0:
                if sumCol == K:
                    total += 1
                sumCol = 0
        if sumCol == K:
            total += 1
    print("#{} {}".format(i, total))