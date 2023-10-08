user_string = input("Введите строку ")
uSSet = set(user_string)
uSSet.discard(" ")
symbol = ""
max_count = -1
for i in uSSet:
    a = user_string.count(i)
    if a > max_count:
        symbol = i
        max_count = a
print(symbol, max_count)