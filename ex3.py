number = input("Введите число от 1 до 1000 ")
if len(number) < 4:
    number = "0" * (3 - len(number)) + number
    txt_number = []
    if number[0] == "1":
        txt_number.append("сто")
    elif number[0] == "2":
        txt_number.append("двести")
    elif number[0] == "3":
        txt_number.append("триста")
    elif number[0] == "4":
        txt_number.append("четыреста")
    elif number[0] == "5":
        txt_number.append("пятьсот")
    elif number[0] == "6":
        txt_number.append("шестьсот")
    elif number[0] == "7":
        txt_number.append("семьсот")
    elif number[0] == "8":
        txt_number.append("восемьсот")
    elif number[0] == "9":
        txt_number.append("девятьсот")

    if number[1] == "1":
        if number[2] == "1":
            txt_number.append("одиннадцать")
        elif number[2] == "2":
            txt_number.append("двеннадцать")
        elif number[2] == "3":
            txt_number.append("триннадцать")
        elif number[2] == "4":
            txt_number.append("четырнадцать")
        elif number[2] == "5":
            txt_number.append("пятнадцать")
        elif number[2] == "6":
            txt_number.append("шестнадцать")
        elif number[2] == "7":
            txt_number.append("семнадцать")
        elif number[2] == "8":
            txt_number.append("восемнадцать")
        elif number[2] == "9":
            txt_number.append("девятнадцать")
    elif number[1] == "2":
        txt_number.append("двадцать")
    elif number[1] == "3":
        txt_number.append("тридцать")
    elif number[1] == "4":
        txt_number.append("сорок")
    elif number[1] == "5":
        txt_number.append("пятьдесят")
    elif number[1] == "6":
        txt_number.append("шестьдесять")
    elif number[1] == "7":
        txt_number.append("семьдесять")
    elif number[1] == "8":
        txt_number.append("восемьдесят")
    elif number[1] == "9":
        txt_number.append("девяносто")

    if number[1] != "1":
        if number[2] == "1":
            txt_number.append("один")
        elif number[2] == "2":
            txt_number.append("два")
        elif number[2] == "3":
            txt_number.append("три")
        elif number[2] == "4":
            txt_number.append("четыре")
        elif number[2] == "5":
            txt_number.append("пять")
        elif number[2] == "6":
            txt_number.append("шесть")
        elif number[2] == "7":
            txt_number.append("семь")
        elif number[2] == "8":
            txt_number.append("восемь")
        elif number[2] == "9":
            txt_number.append("девять")

    print(" ".join(txt_number))
else:
    print("тысяча")