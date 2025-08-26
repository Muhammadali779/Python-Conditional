vazn = float(input("Vazningizni kiriting (kgda): "))
boy = float(input("Bo‘yingizni kiriting (m-da): "))
                                             #bo`y shu oraliqda bo`lishi kerak
if vazn <= 0 or boy <= 0 or vazn > 500 or not (0.5 <= boy <= 3.0):
    print("Noto‘g‘ri qiymatlar kiritildi!")

else:
    bmi = vazn / (boy ** 2)
    print("BMI:", round(bmi, 2))

    if bmi < 18.5:
        print("Kam vazn")

    elif bmi < 25:
        print("Normal vazn")

    elif bmi < 30:
        print("Ortiqcha vazn")
        
    else:
        print("Semizlik")
