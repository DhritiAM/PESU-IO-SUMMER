# Sum of the digits of a given integer

n = int(input("Enter an integer"))
sum = 0
while n > 0:
    x = n%10
    sum+=x
    n = int(n/10)

print("The sum is:",sum)