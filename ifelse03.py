name_file = "musiqalar"

file = input("Fayl nomini kiriting: ")

if name_file in file and len(name_file) == 9 :
    print(f"{file} nomli Fayl mavjud. ")
else:
    print(f"{file} nomli Fayl topilmadi !")
