try:
     num1 = float(input("กรอกตัวเลขที่ 1 "))
     num2 = float(input("กรอกตัวเลขที่ 2 "))
     oparetor = input("เครื่องหมาย + - * /")

     if oparetor =="+":
          result = num1 + num2  

     elif oparetor =="-":
          result = num1 - num2

     elif oparetor =="*":
          result = num1 * num2
     elif oparetor =="/":
          result = num1 / num2
     else:
          raise ValueError("ต้องเป็นเครื่องหมาย + - * /")
     print(f"{num1} {oparetor} {num2} = {result}")
except ZeroDivisionError:
     print("ไม่สามารถหารด้วย 0 ได้")
except ValueError:
     print("กรอกตัวเลขเท่านั้น")
finally:
     print("จบการทำงาน")