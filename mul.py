print("Program to Multiply number without using * Operator")
num1 = int(input("Please Enter a Number:"))
num2 = int(input("Please Enter a Number:"))
sum = 0
for i in range(1,num2+1):
    sum = sum + num1
print(f"The Multiplication of {num1} and {num2} is {sum}")