mylist=input("enter a list of number separatted by space:")
mylist=list(map(int,mylist.split()))
sum=0
for num in mylist:
    sum+=num
print("the sum of the number is",sum)
