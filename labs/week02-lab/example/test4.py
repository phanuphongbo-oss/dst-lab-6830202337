print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()

weight = float(input("input weight"))
hight = float(input("input hight (m)"))

BMI = weight / (hight ** 2 )

print(f"BMI IS {BMI}")