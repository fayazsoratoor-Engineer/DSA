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