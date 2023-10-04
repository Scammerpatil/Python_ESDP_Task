num = int(input("Please Enter a number:"))
sum = 0
back = num
while num!=0:
    temp = num%10
    sum = sum*10+temp
    num = num//10
if back == sum:
    print(f"The given number {back} is Palindrome")
else:
    print(f"The given number {back} is not Palindrome")