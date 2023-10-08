s = list(input("Введите строку "))
sI = list()
for i in range(len(s)):
    if s[i].isalpha():
        s[i] = " " + s[i][0] + " "
s = "".join(s)
s = s.split()
c = 0
while c < len(s) - 1:
    a1 = s[c]
    a2 = s[c + 1]
    if a2.isdigit():
        sI += a1 * int(a2)
        c += 2
    elif a2.isalpha():
        sI += a1
        c += 1
print("".join(sI))