a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))

amal = input("Amalni kiriting (+, -, *, /): ")

if amal == "+":
    print(f"Natija: {a} + {b} = {a+b}")

elif amal == "-":
    print(f"Natija: {a} - {b} = {a-b}")

elif amal == "*":
    print(f"Natija: {a} * {b} = {a*b}")

elif amal == "/":
    if b == 0:
        print("Nolga bo‘lish mumkin emas!")

    else:
        print(f"Natija: {a} / {b} = {a/b}")
        
else:
    print("Noto‘g‘ri amal. Faqat +, -, *, / ishlatiladi.")
