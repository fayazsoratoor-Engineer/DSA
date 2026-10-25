def dup(str):
    new_str=""
    for i in str:
        if i not in new_str:
            new_str+=i
    return new_str  
print(dup("hello world"))

def hi(str):
    for i in str:
        if i==" ":
            str=str.replace(" ","-")
    return str
print(hi("hello world"))


def hi(str):
    count=0
    for i in str:
        if i==" ":
            count+=2
    return count
print(hi("hello world fayaz"))


