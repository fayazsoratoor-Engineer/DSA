#O(n) time complexity
L=[1,2,3,4,5]

sum=0
for i in L:
    sum+=i
print(sum)

#O(n) time complexity
product=1
for i in L:
    product*=i
print(product)

#O(n^2) time complexity
L=[1,2,3,4,5]

for i in L:
    for j in L:
        print("({},{})".format(i,j))
#O(log n) time complexity
def intstr(i):
    digits="0123456789"
    if i ==0:
        return 0
    result=""
    while i>0:
        result=digits[i%10]+result
        i//=10

    return result
a=intstr(456)
print(a)
print(type(a))

#O(n) time complexity
L=[1,2,3,4,5]
for i in range(len(L)//2):
    other=len(L)-1-i
    L[i],L[other]=L[other],L[i]
print(L)

#O(n) time complexity
def fact(n):
    if n==0:
        return 1
    facts=fact(n-1)*n
    return facts

print(fact(5))

#O(n^2) time complexity or O(1.7^n)
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(19))


#O(1) time complexity
def mod(a,b):
    if b<=0:
        return -1
    else:
        div=a//b
        return a-div*b
print(mod(10,3))

#O(log n) time complexity
def sum_digits(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10  
    return sum
print(sum_digits(123456789))


lists=[1,2,3,4,5]
print(id(lists[0]))
print(id(lists[1]))


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


#O(n) time complexity
L=[1,2,3,4,5]

sum=0
for i in L:
    sum+=i
print(sum)

#O(n) time complexity
product=1
for i in L:
    product*=i
print(product)

#O(n^2) time complexity
L=[1,2,3,4,5]

for i in L:
    for j in L:
        print("({},{})".format(i,j))
#O(log n) time complexity
def intstr(i):
    digits="0123456789"
    if i ==0:
        return 0
    result=""
    while i>0:
        result=digits[i%10]+result
        i//=10

    return result
a=intstr(456)
print(a)
print(type(a))

#O(n) time complexity
L=[1,2,3,4,5]
for i in range(len(L)//2):
    other=len(L)-1-i
    L[i],L[other]=L[other],L[i]
print(L)

#O(n) time complexity
def fact(n):
    if n==0:
        return 1
    facts=fact(n-1)*n
    return facts

print(fact(5))

#O(n^2) time complexity or O(1.7^n)
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(19))


#O(1) time complexity
def mod(a,b):
    if b<=0:
        return -1
    else:
        div=a//b
        return a-div*b
print(mod(10,3))

#O(log n) time complexity
def sum_digits(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10  
    return sum
print(sum_digits(123456789))


lists=[1,2,3,4,5]
print(id(lists[0]))
print(id(lists[1]))


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
