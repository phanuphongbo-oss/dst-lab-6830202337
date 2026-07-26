print("จะแลกเงินอะไร")
print("1.bath to usd")
print("2.usd to bath")

choice = int(input(": "))

money = int(input("กรอกจำนวนเงิน :"))

if choice == 1:
    total = money/35.5
    print(f"จำนวนเงินที่ได้ {total:.2f} ดอลล่า")
    print("สูตรที่ใช้ หาร่ 35.5")
elif choice == 2:
    total = money*35.5
    print(f"จำนวนเงินที่ได้ {total:.2f} บาท")
    print("สูตรที่ใช้ คูณ 35.5")

    