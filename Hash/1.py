student={
    "name": "John Doe",
    "age": 20,
}

def two(str,target):

    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if str[i]+str[j]==target:
                return [i,j]
print(two([2,7,11,15],9))



def repeat(str):

    seen={}
    for i in str:
        if i not in seen:
            print(i)
            seen[i]=1   
print(repeat("hello world"))