print("Program to print number of digits")
num = int(input("Enter a Number:"))
back = num
count = 0
while num !=0:
    count +=1
    num = num//10
if count>=5:
    print(f"Please Enter a number upto 5 digits")
else:
    print(f"The given number {back} has {count} no. of digits")
