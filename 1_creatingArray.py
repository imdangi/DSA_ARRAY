# Here we are not using list predefined function , we will make pure logic of array
n = int(input("Enter how many elements you want to add in array : "))
arr = []
for i in range(n):
    temp = int(input(f"Enter value  {i+1} of array : "))
    arr.append(temp) #--> list will overwrite with new values every time , and we will have only last element
                    #--> this is same as scanf("%d",&arr[i]); in c
# Printing values of array , Traversal operation
for i in arr:
    print(i, end=" ")
print("Printing Again with another way of using for loop in python :- ")
for i in range(n):
    print(arr[i],end=" ")


