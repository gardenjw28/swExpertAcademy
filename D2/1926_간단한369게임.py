N = int(input())
total = ""
n = 0
for i in range(1, N+1):
    for ii in str(i):
        n += ['3', '6', '9'].count(ii)
    if n == 0:
        total = total + str(i) + " "
    else:
        total = total + ("-"*n) + " "
        n = 0
print(total)