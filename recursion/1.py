def count(n):
    if n == 0:
        return 
    count(n-1)
    print(n)
count(5)



def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
for i in range(7):
    print(fibonacci(i), end=" ")

def power(a,n):
    if n == 0:
        return 1
    return a * power(a,n-1)
print(power(2,3))


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    if root is None:
        return

    print(root.value, end=" ")
    preorder(root.left)
    preorder(root.right)
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.value, end=" ")
    inorder(root.right)
def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.value, end=" ")
root = Node(1)
root.left = Node(2)
root.right = Node(3)

preorder(root)
inorder(root)
postorder(root)


def subsets(arr, index=0, current=None):
    if current is None:
        current = []

    if index == len(arr):
        print(current)
        return

    subsets(arr, index + 1, current)

    subsets(arr, index + 1, current + [arr[index]])

subsets([1, 2,3])

def permutations(arr, current=None):
    if current is None:
        current = []

    if len(arr) == 0:
        print(current)
        return

    for i in range(len(arr)):
        permutations(
            arr[:i] + arr[i + 1:],
            current + [arr[i]]
        )

permutations([1, 2, 3])


def  search(arr,target):
    left=0
    right=len(arr)-1

    while left <=right:
        mid=(left+right)//2

        if arr[mid]==target:
            return mid 

        if arr [mid]<target:
            left+=1

        else:
            right-=1
    return -1
arr=[1,2,3,3,4,5]
print(search(arr,3))

def search(arr,target):
    left=0
    right=len(arr)-1

    while left <=right:
        mid=(left+right)//2

        if arr[mid]==target:
            return mid 

        if arr [mid]<target:
            left+=1

        else:
            right-=1
    return -1
print(search([1,2,3,4,5,6,7,8,9],5))