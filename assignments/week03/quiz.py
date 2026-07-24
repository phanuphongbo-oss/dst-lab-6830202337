# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:

if age >= 0 and age <= 12 :
    print("Child")
elif age >= 13 and age <=19 :
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")        
elif age >= 60 :
    print("Senior")

# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            print(f"Balance is {balance} bath")
        elif choice == "2":
             withdraw = int(input("กรอกจำนวนเงิน"))
             balance = balance - withdraw
             print(f"Balance remaining {balance} bath")     
        elif choice == "3":
            Deposit = int(input("กรอกจำนวนเงิน"))
            balance = balance + Deposit
            print(f"Balance remaining {balance} bath")
        elif choice == "4":
            break
else:
    print("Invalid PIN")
