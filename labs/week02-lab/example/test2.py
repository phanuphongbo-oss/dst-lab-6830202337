print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

time = int(input("input your time"))

hour = time // 3600 
second_remin = time % 3600

minute = second_remin // 60
second_remain = minute % 60

print(f"second = {hour},{minute},{second_remain}")