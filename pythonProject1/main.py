import os

day = int(input("Enter Your Date : "))
sign = ""
if  day > 0 and (day <= 30 or day == 31):
    month = input("Enter Month Name : ")
    if month.lower() == "march":
        if day >= 21:
            sign = "Aries"
        else:
            sign = "Picses"
    elif month.lower() == "april":
        if day >= 20:
            sign = "Taurus"
        else:
            sign = "Aries"
    else:
        sign = "Invalid Month"
else:
    os.system('cls')
    print("Invalid Date")
    exit(0)


os.system('cls')
print(sign)



