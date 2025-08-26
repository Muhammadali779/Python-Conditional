soat = int(input("Soatni kiriting: "))

if 5 <= soat <= 11:
    print("Ertalab")

elif 12 <= soat <= 17:
    print("Kunduzi")

elif 18 <= soat <= 21:
    print("Kechqurun")

elif (22 <= soat <= 23) or (0 <= soat <= 4):
    print("Tun")
    
else:
    print("Soat 0-23 oralig‘ida bo‘lishi kerak!")


