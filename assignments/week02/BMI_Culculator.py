
weight= int(input("กรอกน้ำหนัก(kg)"))
height = float(input("กรอกส่วนสูง(m) "))
BMI = weight / height**2

print(f"BMI : {BMI:.1f}")

if BMI <= 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal weight")
elif BMI >= 25 and BMI <= 29.9:
    print(" Overweight")
elif BMI >= 30.0:
    print(" Obese")