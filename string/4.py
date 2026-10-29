def long(str):

    str1=str.split(" ")
    longest=""

    for i in str1:
        if len(i)>len(longest):
            longest=i
    return longest
print(long("hello worlgd fayaz"))



words = ["flower", "flow", "flight"]

prefix = words[0]

for word in words:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print(prefix)



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
