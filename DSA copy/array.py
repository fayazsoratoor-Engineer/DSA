#Largest number in the list
lists=[4,2,3,2,101,1,6,7,8,9]
largest=lists[0]
for i in lists:
    if i>largest:
        largest=i
print("Largest number in the list:",largest)    

#Smallest number in the list
lists=[4,2,3,2,101,1,6,7,8,9,-1987847]
largest=lists[0]
for i in lists:
    if i<largest:
        largest=i
print("Smallest number in the list:",largest)    

#sum of the list
lists=[4,2,3,2,101,1,6,7,8,9]
sums=0
for i in lists:
    sums+=i
print("Sum of the list:",sums)

#average of the list
lists=[4,2,3,2,101,1,6,7,8,9]
sums=0
for i in lists:
    sums+=i
print("Average of the list:",sums/len(lists))



lists=[4,2,3,2,101,1,6,7,8,9]
even=0
odd=0
for i in lists:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Number of even numbers in the list:",even)
print("Number of odd numbers in the list:",odd)



#Largest number in the list
lists=[4,2,3,2,101,1,6,7,8,9]
largest=lists[0]
for i in lists:
    if i>largest:
        largest=i
print("Largest number in the list:",largest)  


arr=[4,2,3,2,101,1,6,7,8,9]
print(arr.index(101))
print(id(arr[0]))
print(id(arr[1]))

a=[1,2,3,4,5]
b=a.copy()
b[0]=100
print(a)
print(b)

num=list(range(1,11,2))
print(num)

num=list("Hello World")
print(num)


from array import array
arr=array('i',[1,2,3,4,5])
print(type(arr))
print(arr[0])
print(arr)

letters=['a','b','c','d','e']
for i, j in enumerate(letters):
    print(f"Index: {i}, Value: {j}")
print(letters[2:-5:-1])


def maggi():
    for i in range(1,11):
        for j in range(1,11):
            print(f"{i}x{j}={i*j}")
maggi()