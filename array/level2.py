def missing_number(arr):
    n=len(arr)
    expected_sum=n*(n+1)//2
    actual_sum=sum(arr)
    return expected_sum-actual_sum
print(missing_number([0,1,2,3,4,6,8]))  # Output: 5


def move(arr):

    for i in arr:
        if i==0:
            arr.remove(i)
            arr.append(i)
    return arr
print(move([1,0,2,0,3,0,4]))  #

def rotate(arr,k):
    n=len(arr)
    k=k%n
    return arr[-k:]+arr[:-k]
print(rotate([1,2,3,4,5,6,7,8,9,10],9))  # Output: [4, 5, 1, 2, 3]

def merge(arr1,arr2):
    return sorted(arr1+arr2)
print(merge([1,2,9,3],[4,5,6]))  # Output: [1, 2, 3, 4, 5, 6, 9]

def intersection(arr1,arr2):
    return list(set(arr1)&set(arr2))
print(intersection([1,2,3,4,5],[4,5,6,7,8]))  # Output: [4, 5]

def two_sum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return (i, j)
print(two_sum([1,2,3,4,5],7))  # Output: (2, 5)

def duplicate(arr):

    duplicate=[]
    for i in arr:
        if arr.count(i)>1 and i not in duplicate:
            duplicate.append(i)
    return duplicate
print(duplicate([1,2,3,4,5,3,3,3]))  # Output: [3, 3, 3]

def majority_element(arr):

    for i in arr:
        if arr.count(i)>len(arr)//2:
            return i
    return -1

print(majority_element([2, 2, 1, 2, 3, 2, 2]))