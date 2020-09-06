t = int(input())
cost = [50000,10000,5000,1000,500,100,50,10]
for i in range(1, t+1):
    N = int(input())
    costCount = list( 0 for i in range(8))
    for c in range(len(cost)):
        if N // cost[c] == 0:
            N = N
        else:
            costCount[c] = N // cost[c]
            N = N % cost[c]
    print("#{}".format(i))
    print(" ".join(str(count) for count in costCount))