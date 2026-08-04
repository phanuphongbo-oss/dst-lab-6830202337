list = []
for i in range(5):
    score = int(input("Enter score of student :"))
    list.append(score)
for i in range(5):
    if list[i] < 49 :
        print(f"student {i+1}: {list[i]} ไม่ผ่าน")
    if list[i]>= 50 :
        print(f"student {i+1}: {list[i]} ผ่าน")
        