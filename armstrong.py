print("Program to print Armstrong number from 1 to 9000")
for i in range(1,9000):
    num  = i
    count = 0
    sum = 0
    while num!=0:
        count+=1
        num = num//10
    num = i
    while num !=0:
        temp = num % 10
        power = temp ** count
        # print(i, power)
        # print(type(power))
        sum = sum + power
        num = num//10
    if sum == i:
        print(i,end=" ")

