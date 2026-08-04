item = []
new_item = []
print("Enter prices of 6 item :")
for i in range(6):
    Item = int(input(f"item {i+1}: "))
    item.append(Item)
budget = int(input("Enter total budget : "))

total = 0

for i in range(6):
    if total+item[i] <= budget:
     total+=item[i]
     print(f"item {i+1} = {item[i]} buy")
     print(f"Current total = {total}")
     new_item.append(item[i])
    else:
     print(f"item {i+1} = {item[i]} cannot buy")
     print(f"Current total = {total}")

print(f"Bought item: {new_item}")
print(f"Total spent: {total}")
print(f"Remaining budget: {budget-total}")


