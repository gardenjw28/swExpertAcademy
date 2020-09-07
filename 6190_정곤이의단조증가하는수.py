T = int(input())
for t in range(1, T+1):
    N = int(input())
    numList = list(map(int, input().split()))

    multiList = list() #곱한 값 리스트
    for a in range(len(numList)-1):
        for b in range(a+1, len(numList)):
            multiList.append(numList[a]*numList[b])

    for multiIdx in range(len(multiList)): #곱한 값들 index 들고오기
        multi = str(multiList[multiIdx]) #자리 수 비교해야하니까 곱한 값 string으로 만들기
        currentMulti = multi[0] #가져온 곱한 값 첫번째 자리를 current로 할당

        for i in range(1, len(multi)):
            if currentMulti <= multi[i]: #단조
                currentMulti = multi[i]
            else: #단조 아닐 때 currentMulti > multi[i]
                multiList[multiIdx] = -1
    maxMulti = max(multiList)
    print("#{} {}".format(t, maxMulti))