#Largest Number
def find_largest(arr):

    #1 senario List is Empty
    if len(arr)==0:
        return "array is Empty"
    largest=arr[0]
    index=0

    #2 senario 
    if len(arr)==1:
        return arr[0]

    
    for i in range(len(arr)):
        if arr[i] > largest:
            largest=arr[i]
            index=i
    print("index=",index,end=" ")
    print("Largest_number=",largest)
    return largest

def excute_largest_number(n):
    number=[]
    
    for i in range(n):
        value=int(input("enter number"))
            
            
        number.append(value)
    find_largest(number)
    

# excute_largest_number(5)


def find_smallest(arr):

    #1 senario List is Empty
    if len(arr)==0:
        return "array is Empty"
    smallest=arr[0]
    index=0

    #2 senario 
    if len(arr)==1:
        return arr[0]

    
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest=arr[i]
            index=i
    print("index=",index,end=" ")
    print("smallest_number=",smallest)
    return smallest
def excute_smallest_number(n):
    number=[]
    
    for i in range(n):
        value=int(input("enter number"))
            
            
        number.append(value)
    find_smallest(number)
    

# excute_smallest_number(5)


'''second_largest_distinct_element'''
def second_largest_distinct_element(arr):
    #1 senario List is Empty
    if len(arr)==0:
        return "Empty array"
    elif len(arr)<2:
        return "No second largest element"

    largest=float("-inf")
    second=float("-inf")

    for num in range(0,len(arr)):
        if arr[num]>largest:
            second=largest
            largest=arr[num]
        elif arr[num]>second and arr[num]!=largest:
            second=arr[num]
        

    if second==float("-inf"):
        return "no Second largest Distinct"

    inddex=arr.index(second)
    print("index=",inddex,end=" ")
    print("Second_Largest_number=",second)
    return second


def excute_second_largest_number(n):
    number=[]
    
    for i in range(n):
        value=int(input("enter number:"))
            
            
        number.append(value)
    second_largest_distinct_element(number)


# print(excute_second_largest_number(5))

''''''
def second_smallest_distinct_element(arr):
    #1 senario List is Empty
    if len(arr)==0:
        return "Empty array"
    elif len(arr)<2:
        return "No second smallest element"

    smallest=float("inf")
    second=float("inf")

    for num in range(0,len(arr)):
        if arr[num]<smallest:
            second=smallest
            smallest=arr[num]
        elif arr[num]<second and arr[num]!=smallest:
            second=arr[num]
        

    if second==float("-inf"):
        return "no Second largest Distinct"

    index=arr.index(second)
    print("index=",index,end=" ")
    print("Second_smallest_number=",second)
    


def excute_second_smallest_number(n):
    number=[]
    
    for i in range(n):
        value=int(input("enter number:"))
            
            
        number.append(value)
    second_smallest_distinct_element(number)


# excute_second_smallest_number(5)


'''4.calculate the sum of all element'''
def Sum_of_all_element(arr):
    sum=0
    if len(arr)==0:
        return "Array is Empty"
    elif len(arr)==1:
        return arr[0]

    for i in arr:
        sum+=i

    print("Sum_of_all _element",sum)

# Sum_of_all_element([10,20,30,40,50])


'''5. Count even and odd numbers'''

def Count_even_And_odd(arr):
    if len(arr)==0:
        return "Array is Empty"
    even=0
    odd=0
    for u in arr:
        if u %2==0:
            even+=1
        else:
            odd+=1   
    return even,odd

# print(Count_even_And_odd([1,2,3,4,5,6,7,8,9,4,5,1,2]))
# print(Count_even_And_odd([ ]))

'''6. Reverse an array without reverse()'''
def Reverse_array(arr):
    if len(arr)==0:
        return "Array is Empty"
    elif len(arr)==1:
        return arr

    for i in range(len(arr)//2):
        other=len(arr)-i-1
        arr[i],arr[other]=arr[other],arr[i]
    return arr
def excute():
    print(Reverse_array([1,2,3,4,5]))
    print(Reverse_array([]))
    print(Reverse_array([1,8]))

''' 7. Search for an element'''
def Search(arr,key):
    if len(arr)==0:
        return "array is Empty"
    elif len(arr)==1:
        return arr[0]

    for index in range(len(arr)):
        if arr[index]==key:
            return index

    return -1

def excute_search():
    arr = [10, 20, 30, 40, 50]
    target = 30

    result = Search(arr, target)

    if result == -1:
        print("Element not found")
    elif result == "Array is empty":
        print(result)
    else:
        print("Element found at index", result)

'''8 Remove duplicates from an array'''

def Remove_duplicate(arr):
    if len(arr)==0:
            return "array is Empty"

    elif len(arr)==1:
        return arr[0]

    sets=set(arr)
    return sets
def excute_remove():
    arr=[1,23,1,2,12,1,2,1,2]
    call=Remove_duplicate(arr)
    print(list(call))

'''9 Count the occurrences of each element'''
def occurence(arr):
    if len(arr)==0:
        return "array is Empty"
    elif len(arr)==1:
        return f"{arr[0]}occurence 1 times"

    visited=[]
    for i in arr:
        if i not in visited:
            count=0

            for value in arr:
                if value==i:
                    count+=1

            print(i,"occurs",count,"times")
            visited.append(i)
# occurence([1,2,12,1,2,12,1,21,21,2,12])

'''9 Count the occurrences of each element'''

arr = [5, 5, 2, 3, 2, 5, 4]

frequency = {}

for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# print(frequency)

'''10 Move all zeros to the end'''

def all_zero_to_end(arr):
    if len(arr)==0:
        return "array is Empty"
    elif len(arr)==1:
        return arr

    zeros=arr.count(0)

    for i in range(zeros):
        arr.remove(0)

    arr.extend([0]*zeros)
    return arr

# print(all_zero_to_end([0,1,0,1,0,1,2,1,2]))

def Missing_number(arr):
    if len(arr)==0:
        return "array is Empty"
    elif len(arr)==1:
        return arr

    for i in range(1,len(arr)+1):
        if i not in arr:
            print("missing number",i)
Missing_number([1,2,3,4,5,6,7,9])

'''20 two Pointer'''

def Two_pointer(arr,target):
    left=0
    right=len(arr)-1

    while left <right:
        total=arr[left]+arr[right]

        if total == target:
            print(arr[left],arr[right])
            break

        elif total < target:
            left+=1

        else:
            right+=1

Two_pointer([1,2,3,4,8,9],11)


''' 21 Maximum nmumber'''
def Number(arr):
    k=3
    Window_sum=sum(arr[:k])
    maximum=Window_sum

    for i in range(k,len(arr)):
        Window_sum+=arr[i]
        Window_sum-=arr[i-k]

        maximum=max(maximum,Window_sum)
    return maximum
print(Number([1,2,8,5,7,5,1,2,3]))


