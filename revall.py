print("Program to print Reverse of number from 101 to 10000")
for i in range(101,100001):
    back = i
    back1 = i
    sum = 0 
    while back1 !=0:
        temp = back1 % 10
        sum = sum*10 + temp
        back1 = back1//10
    print(f"The Reverse of {back} is {sum}")
