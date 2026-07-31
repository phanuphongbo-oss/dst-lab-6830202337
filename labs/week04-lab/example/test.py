input = input("what is your name :")
count = 0
for i in  input:
    if i =='a' or i =='A':
     count = count + 1
    if i =='e' or i =='E':
        count = count + 1
    if i =='i' or i =='I':
     count = count + 1
    if i =='o' or i =='O':
     count = count + 1
    if i =='u' or i =='U':
     count = count + 1

print(f"eiou :{count}")
