#linear search is a simple search algorithm that checks every element in a list sequentially until the desired element is found or the list ends. It is easy to implement but can be inefficient for large datasets, as it has a time complexity of O(n).

def LinearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [1, 2, 3, 3, 4, 5]
print(LinearSearch(arr, 3))  # Output: 2


def Binarysearch(arr,target):
    left=0
    right=len(arr)-1

    while left <=right:
        mid=(left+right)//2

        if arr[mid]==target:
            return mid
        if arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

arr = [
    5, 10, 15, 20, 25, 30, 35, 40, 45, 50,
    55, 60, 65, 70, 75, 80, 85, 90, 95, 100,
    105, 110, 115, 120, 125, 130, 135, 140, 145, 150,
    155, 160, 165, 170, 175, 180, 185, 190, 195, 200,
    205, 210, 215, 220, 225, 230, 235, 240, 245, 250
]

target = 180
print(Binarysearch(arr, target))  # Output: 32


low = 1
high = 100

print("Think of a number between 1 and 100!")

while low <= high:
    mid = (low + high) // 2

    print("Is your number", mid, "?")
    answer = input("Enter h for higher, l for lower, c for correct: ")

    if answer == "c":
        print("I found your number!")
        break
    elif answer == "h":
        low = mid + 1
    elif answer == "l":
        high = mid - 1
    else:
        print("Invalid input. Try again.")
