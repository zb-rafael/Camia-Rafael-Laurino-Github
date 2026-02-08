# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print("Program started")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hello, GitHub!")  # Press Ctrl+F8 to toggle the breakpoint.
name = input("Enter your name: ")
print("Hello", name)

try:
    age = int(input("Enter your age: "))
    print("You are", age)
except ValueError:
    print("Invalid Input")

def add(a, b):
    return a + b
    
num1 = int(input("Enter first number:")
num2 = int(input("Enter second number:")
           
result = add(num1, num2)
print("The sum is", result)
    
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Pycharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
