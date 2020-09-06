TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    wireList = list()
    for n in range(N):
        wireList.append(list(map(int, input().split())))
    total = 0
    for currentWire in wireList:
        for compareWire in wireList:
            if (currentWire[0] < compareWire[0] and currentWire[1] > compareWire[1]) or  (currentWire[0] > compareWire[0] and currentWire[1] < compareWire[1]):
                total += 1
    print("#{} {}".format(tc, int(total/2)))