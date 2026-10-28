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