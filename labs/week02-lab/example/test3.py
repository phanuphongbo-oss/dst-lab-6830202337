# Template 3: Shopping Calculator
shopping_calculator = '''
# Shopping Calculator Template

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

# TODO: Calculate subtotal
# TODO: Calculate discount amount
# TODO: Calculate price after discount
# TODO: Calculate tax amount
# TODO: Calculate final total
# TODO: Display itemized receipt
'''

print("Copy these templates to practice!")

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))



# TODO: Calculate subtotal
total = item_price * quantity

# TODO: Calculate discount amount
discount = total *(discount_percent/100)

# TODO: Calculate price after discount
price = total - discount

# TODO: Calculate tax amount
tax_amount = price * (tax_percent/100)

# TODO: Calculate final total
final = price + tax_amount

# TODO: Display itemized receipt
print(f"total{total}")
print(f"discount{discount}")
print(f"tax_amount{tax_amount}")
print(f"final{final}")


