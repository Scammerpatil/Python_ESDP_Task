print("Program to find sum in a series")
print("The series is\n1+x/1!+x^2/2!.....+x^n/n!")
x = int(input("Please enter the number whose sum is to be find:"))
n = int(input("Please Enter the range:"))
sum = 1
def fact(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    return fact
for i in  range(1,n+1):
    sum += (x**i)/fact(i)
print(f"The sum of series of {x} in {n} range is {sum}")