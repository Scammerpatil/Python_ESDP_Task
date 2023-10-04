num = int(input("Please Enter a number:"))
sum = 0
back = num
while num!=0:
    temp = num%10
    sum = sum*10+temp
    num = num//10
print(f"The Reverse of {back} is {sum}")
print(f'The -2 of {sum} is {sum-2}')