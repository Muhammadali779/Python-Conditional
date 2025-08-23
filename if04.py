narx = 100_000

age = int(input("Yoshingizni kiriting: "))

if age > 0 and age < 7:
    narx = narx*0.5
    print("7 yoshgacha (0-6): 50% chegirma NArxi: ",narx)

if age >= 7 and age <=17 :
    narx = narx*0.8
    print("7-17 yosh: 20% chegirma NArxi: ",narx)

if age > 17 and age < 60:
    print("Siz kabi yoshdagilarga chegirma yo`q NArxi: ",narx)

if age >= 60:
    narx = narx*0.7
    print("60 yoshdan katta: 30% chegirma NArxi: ",narx)