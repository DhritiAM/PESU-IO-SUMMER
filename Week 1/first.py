# Taking input and displaying it as a list and tuple

a = input("Enter the numbers")
print(a)
a = a.split(",")
b = []
for i in a:
    b.append(int(i))
print(b)
c = tuple(b)
print(c)