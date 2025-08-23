#4 ga bo`linish qoidasi oxirgi 2ta xonasi 4 ga qoldiqsiz bo`linsa u son 4ga bo`linadi

son = int(input("Son kiriting: "))
x = son % 100

if x % 4 == 0 or son % 4 == 0:
    print("Kiritgan soningiz 4 ga bo'linadi")
