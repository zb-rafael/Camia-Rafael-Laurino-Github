# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hello, GitHub!")  # Press Ctrl+F8 to toggle the breakpoint.

print("Program started")

# Greets User
name = input("Enter your name: ")
print("Hello", name)

# Age Function
try:
    age = int(input("Enter your age: "))
    print("You are", age)
except ValueError:
    print("Invalid Input")

# Addition Calculator
def add(a, b):
    return a + b
    
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

result = add(num1, num2)
print("The sum is", result)

# Decimal to Percentage Calculator
decimal = float(input("Enter a decimal number"))
percentage = decimal * 100
print(f"{decimal} as a percentage is {percentage}% ")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Pycharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
