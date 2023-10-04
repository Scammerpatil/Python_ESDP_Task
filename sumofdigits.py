print("Program to print sum of digits")
num = int(input('Please Enter a number:'))
back = num
sum = 0
while num!=0:
    temp = num % 10
    sum +=temp
    num = num//10
if sum>=20 and sum<=30:
    temp = sum
    sub = 0
    while sum!=0:
        temp1 = sum%10
        if temp1>sub:
            sub = temp1 - sub
        else:
            sub -=temp1
        sum = sum//10
    print(f"The sum of digits of {back} is between 20 and 30 i.e., {temp}\nThus, subtraction of digits of {temp} is {sub}")
else:
    print(f"The sum of digits of {back} is {sum}")



