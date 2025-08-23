harorat = float(input("Haroratni kiriting: "))

if harorat < 0:
    print("Juda sovuq! Issiq kiyim kiying.")

if 0 <= harorat and harorat <= 14:
    print("Sovuq! Kurtka kiying.")

if  harorat > 14 and harorat < 15 :
    print("Ob - Havo O`rtacha.")

if  harorat >= 15 and harorat <60:
    print("Ob - Havo yaxshi.")   

if  harorat >= 60 :
    print("Havo Yondiryabdi ")  