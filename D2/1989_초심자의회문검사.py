def palindrome(s):
    ps,ss = "",""
    ss = ""
    for i in range(len(s), 0, -1):
        ps = ps + str(s[i-1])
        ss = ss + str(s[-i])
    if ss == ps:
        return 1
    else:
        return 0

t = int(input())
for i in range(1,t+1):
    test = input()
    c = palindrome(test)
    print("#{} {}".format(i, c))