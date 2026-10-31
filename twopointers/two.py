def reverses(arr):
    left=0
    right=len(arr)-1

    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr

  

print(reverses([1,2,3,4,5,6]))

def target(arr,target):
    left=0
    right=len(arr)-1
    sum=arr[left]+arr[right]
    while left < right:
        if sum==target:
            return [left,right]
        elif sum<target:
            left+=1
        elif sum>target:
            right-=1
        else:
            print("no posiibrl")
    
print(target([1,2,3,4,5,6],8))