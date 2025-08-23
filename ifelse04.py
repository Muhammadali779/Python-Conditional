balans = 5000

sum = int(input("Qanda summa yechmoqchisiz ? "))

if sum <= balans :
    qoldiq = balans- sum
    print(f"Pul yechildi. Qolgan balans: {qoldiq} so'm")

else :
    print("Katta summani yechishga mablag`ingiz yetmaydi.") 
