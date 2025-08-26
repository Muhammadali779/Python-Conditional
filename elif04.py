masofa = float(input("Masofani kiriting: "))

if masofa < 0:
    print("Masofa manfiy bo‘la olmaydi!")

elif masofa <= 1:
    print("Piyoda yuring")

elif masofa <= 5:
    print("Velosiped yoki elektr skuter")

elif masofa <= 50:
    print("Avtobus yoki mashina")
    
else:
    print("Poyezd yoki samolyot")

