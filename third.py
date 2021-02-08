myarr=list(map(int,input().split(",")))
arr=[]
for i in range(len(myarr)):
    if myarr[i]%2==0:
        arr.append(i)
print("\nThe positions of numbers which are divisible by 2 are:",end=" ")
for i in arr:
    print(i,end=" ")
print("\n\n")
print("Note: These positions are according to python and starting from 0")