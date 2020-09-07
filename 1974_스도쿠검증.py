T = int(input())
for t in range(1, T+1):
    testList = list()
    mapList = [list(map(int, input().split())) for _ in range(9)]
    nums = set((1,2,3,4,5,6,7,8,9))

    result = 2
    while result == 2:
        for i in range(9):
            if set(mapList[i]) != nums: #가로
                result = 0
                break

        tempList = list()
        for q in range(9):
            for j in range(9):
                tempList.append(mapList[j][q])
            if set(tempList) != nums:
                result = 0
                break
            else:
                tempList = list()

        compareIdxList = [[0,0],[0,3],[0,6],
                           [3,0],[3,3],[3,6],
                           [6,0],[6,3],[6,6]]
        compareList = list()
        for c in compareIdxList:
            for x in range(3):
                compareList.append(mapList[c[0]+x][c[1]])
                compareList.append(mapList[c[0]+x][c[1]+1])
                compareList.append(mapList[c[0]+x][c[1]+2])
            if set(compareList) != nums:
                result = 0
                break
            else:
                compareList = list()
        if result != 0:
            result = 1
    print("#{} {}".format(t, result))