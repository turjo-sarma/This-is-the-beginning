print("Factorial counter")
a = int(input("Enter the number :"))
fact = 1
for i in range(1,(a + 1)):
    fact *= i
print(f"The factorial of the number {a} is {fact}")

print("Square mode")
b = int(input("Enter the number :"))
print(f"The square of number {b} is {b**2}")