yil = int(input("Yilni kiriting: "))
if yil % 400 == 0:
    print(yil, "- kabisa yili")
if yil % 100 == 0:
    print(yil, "- kabisa yili emas")
if yil % 4 == 0:
    print(yil, "- kabisa yili")
else:
    print(yil, "- kabisa yili emas")

vazn = int(input("Vazn: "))
boy = int(input("Bo'y: "))

bmi = vazn / (boy * boy)

if bmi < 18.5:
    holat = "Vazn yetishmasligi"
if bmi < 25:
    holat = "Normal vazn"
if bmi < 30:
    holat = "Ortiqcha vazn"
else:
    holat = "Semizlik"

print("BMI =", round(bmi, 1), "-", holat)