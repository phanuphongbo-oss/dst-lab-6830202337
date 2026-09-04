


print("\n=== ITERATING THROUGH STRING ===")
text = input("inser your text")
a = input("Character to find")
count = 0
for letter in text:
    if letter == a:
        count += 1
print(f"{count} letters '{letter}' found in '{text}'")

password = input("Enter your password")
lenght = len(password)
words = password.split('0')
if len(words) > 8:
    left = words[0].isalnum()
    right  = words[1].isalnum()  
else :
    left = False;
    right = False;
if lenght >= 8 and len(words) == 2 and left == True and right == True:
    print("password is string")
else:
    print("password is not string")