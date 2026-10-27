def two_pointer(arr,target):
    left=0
    right=len(arr)-1
    while left < right:
        if arr[left]+arr[right]==target:
            return [arr[left],arr[right]]
        elif arr[left]+arr[right]<target:
            left+=1
        else:
            right-=1
print(two_pointer([1,2,3,4,5],7))  # Output

#\[\text{New Sum}=\text{Old Sum}-\text{Outgoing}+\text{Incoming}
def sliding_window(arr,k):

    window_sum=sum(arr[:k])
    max_sum=window_sum
    for i in range(k,len(arr)):
        window_sum=window_sum-arr[i-k]+arr[i]
        if window_sum>max_sum:
            max_sum=window_sum
        
    return max_sum

print(sliding_window([1,2,3,4,5,6],3))  # Output: 9



def max_average_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)  

    max_average = max_sum / k

    return max_average
print(max_average_subarray([1, 12, -5, -6, 50, 3], 4))  # Output: 12.75

def duplicates(arr):
    duplicate=[]
    for i in arr:
        if arr.count(i)>1 and i not in duplicate    :
            duplicate.append(i)
    return duplicate
print(duplicates([1,2,3,4,5,1,2,5,-1,-1]))

def duplicates(arr):
    duplicate=[]
    for i in range(len(arr)):
        if arr.count(arr[i])>1 and arr[i] not in duplicate    :
            duplicate.append(arr[i])
    return duplicate
print(duplicates([1,2,3,4,5,1,2,5,-1,-1]))

def find(arr):
    for i in range(len(arr)):
        if arr.count(arr[i])<2:
            return arr[i]
print(find([1,2,3,4,5,1,2,5,-1,-1]))

def finds(arr):
    frequency={}
    for i in arr:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
        

            for key,value in frequency.items():
                if value==1:
                    return key
print(finds([1,2,3,4,5,1,2,5,-1,-1]))