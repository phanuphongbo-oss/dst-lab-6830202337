
print("\n=== ITERATING THROUGH STRING ===")
text = input("text")
a = input("letter")
count = 0
for letter in text:
    if letter == a:
        count += 1
print(f"{count} letters {a} found in '{text}'")
