def palin(str):
    return str == str[::-1]
print(palin("racecdar"))\

def vowel_count(str):
    vowel=0
    cons=0

    for i in str:
        if i in "aeiouAEIOU":
            vowel+=1
        else:
            cons+=1
    return vowel, cons
print(vowel_count("hello world"))



def fre(str):
    freq={}

    for i in str:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1


    return freq
print(fre("hello world"))

def space(str):
    for i in str:
        if i==" ":
            str=str.replace(" ","")
    return str      

print(space("hello world"))

def non(str):

    for i in str:
        if str.count(i)==1:
            print(i)
            break
    
non("hello world")

def vowel(str):
    vowel=0
    cons=0

    for i in str:
        if i in "aeiouAEIOU":
            vowel+=1
        else:
            cons+=1
    return vowel, cons
print(vowel("hello world"))

def reverse(str):
    return str[::-1]
print(reverse("hello world"))


arr = [2, 5, 8, 12, 15, 19, 24]
target = 15

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Element found at index:", mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")


arr = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum = window_sum - arr[i - k] + arr[i]
    max_sum = max(max_sum, window_sum)

print(max_sum)


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
print(binary_search([1, 2, 3, 4, 5], 3))  # Output: 2
