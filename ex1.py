s = input("Введите строку ")
sI = ""
c = 0
while s != "":
    a = s[c]
    if c + 1 < len(s) and a == s[c + 1]:
        c += 1
    else:
        s = s[c + 1:]
        if c > 0:
            sI += a + str(c + 1)
        else:
            sI += a
        c = 0
print(sI)