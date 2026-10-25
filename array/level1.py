def sums(arr):
    sum = 0
    for i in arr:
        sum+=i
    return sum
print(sums([1,2,3,4,5]))  # Output: 15

def largest(arr):
    largest=arr[0]

    for i in arr:
        if i>largest:
            largest=i
    return largest
print(largest([1,2,3,4,5]))  # Output: 5

def smallest(arr):
    smallest=arr[0]

    for i in arr:
        if i<smallest:
            smallest=i
    return smallest
print(smallest([1,2,3,4,5]))  # Output: 1

def second_largest(arr):
    largest=arr[0]
    second=arr[0]

    for i in arr:
        if i >largest:
            second=largest
            largest=i

        elif i>second and i!=largest:
            second=i
    return second
print(second_largest([1,2,3,4,5]))  # Output: 4


def reverse(arr):
    left=0
    right=len(arr)-1
    while left <right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
print(reverse([1,2,3,4,5]))  # Output: [5, 4, 3, 2, 1]


def check_sorted(arr):

    if arr==sorted(arr):
        return True
    else:
        return False
print(check_sorted([1,3,2,3,3,4,5]))  # Output: True

def counts(arr):
    even=0
    odd=0

    for i in arr:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
print(counts([1,2,3,4,5,6]))  # Output: (


def frequency(arr,target):
    count=0

    for i in arr:
        if i==target:
            count+=1
    return count
print(frequency([1,2,3,4,5,3,3,3],3))  # Output: 3


def occuence(arr,target):

    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
print(occuence([1,2,3,4,5,3,3,3],3))  # Output: 2


def remove_duplicates(arr):
    unique=[]
    for i in arr:
        if i not in unique:
            unique.append(i)
    return unique
print(remove_duplicates([1,2,3,4,5,3,3,3]))  # Output: [1, 2, 4, 5, 3]
print(remove_duplicates([1, 1, 2, 2, 3, 3, 4]))  # Output: [1, 2, 3, 4]
