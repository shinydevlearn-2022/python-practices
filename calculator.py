# calculator.py

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Add and Subtract")

choice = input("Enter choice (1/2/3): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(f"The result is: {add(num1, num2)}")
elif choice == '2':
    print(f"The result is: {subtract(num1, num2)}")
elif choice == '3':
    addition_result = add(num1, num2) 
    subtraction_result = subtract(num1, num2)
    print(f"The result of addition is: {addition_result}")
    print(f"The result of subtraction is: {subtraction_result}")
else:
    print("Invalid choice")
if __name__ == "__main__":
    main()
