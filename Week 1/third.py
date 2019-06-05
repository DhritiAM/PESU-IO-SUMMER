# Binary search

a = input("Enter the numbers")
a = a.split(",")
b = []
for i in a:
    b.append(int(i))
b.sort()
print(b)

def binSearch(a,key):
    low = 0
    high = len(a)-1
    found = 0
    while low<high and found==0:
        mid = int((low+high)/2)
        if key==a[mid]:
            print("The index is:",mid)
            found = 1
        elif key<a[mid]:
            high = mid-1
        else:
            low = mid+1
    if not found:
        print("Element not found in list")
            
n = int(input("Enter the number to be searched"))   
binSearch(b,n)