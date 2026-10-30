'''[ ] 1. Print each character of a string on a separate line.'''
def print_Sprate_line(str):
    if len(str)==0:
        print("String is Empty")
    elif len(str)==1:
        print(str)
    else:
        for i in range(len(str)):
            print(str[i],end="\n")
def Excute_1():

    print_Sprate_line("")
    print_Sprate_line("P")
    print_Sprate_line("Python")

# Excute_1()

'''2 Find the length of a string without using len().'''

def Length_of_string(str):
    if len(str)==0:
        return "String is Empty"
    elif len(str)==1:
        return "length_of_string is 1" 

    else:
        count=0
        for i in str:
            count+=1
    return count

def Excute_2():

    print(Length_of_string(""))
    print(Length_of_string("P"))
    print(Length_of_string("Python"))
# Excute_2()

def Reverse_string(str):

    if len(str)==0:
        return "String is Empty"
    elif len(str)==1:
        return str 
    else:
        revrse=""
        for i in str:
            revrse=i+revrse
        return revrse
def Excute_3():
    print(Reverse_string(""))
    print(Reverse_string("f"))
    print(Reverse_string("fa"))
    print(Reverse_string("Python"))

# Excute_3()

'''4 Count the vowels in a string.'''
def Count_the_vowels(str):
    if len(str)==0:
        print("String is Empty")
    else:
        vowel=0
        const=0
        for i in str:

            if i in "aeiouAEIOU":
                vowel+=1
            elif i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
                const+=1
            else:
                continue
        print("Vowel is",vowel)
        print("Constanets",const)
def Excute_4():
    Count_the_vowels("")
    Count_the_vowels("ee sala cup namde")

# Excute_4()

'''5 Convert lowercase letters to uppercase without using upper().'''
def Convert_letter(str):
    
    if len(str)==0:
        print("String is Empty")
    elif len(str)==1:
        num=ord(str)
        upper=num-32
        print(chr(upper))
    
    else:
        new_string=""
        for i in str:
            num=ord(i)
            upper=num-32
            new_string=new_string+chr(upper)
        print(new_string)
def Excute_5():
    Convert_letter("")
    Convert_letter("g")
    Convert_letter("fayaz")
# Excute_5()

'''6 Check whether a string is a palindrome.'''

def Check_Palindrome(str):
    if len(str)==0:
        print("String is Empty")
    elif len(str)==1:
        print("It is palindrome")
    else:
        if str==str[::-1]:
            print("it is palindrome") 
        else:
            print("it is not palindrome")
def Excute_6():
    Check_Palindrome("")
    Check_Palindrome(" ")
    Check_Palindrome("f")
    Check_Palindrome("fayaz")
    Check_Palindrome("madam")
    Check_Palindrome("gadag")
# Excute_6()

'''7 Count the number of words in a sentence.'''
def Count_Words(str):
        count=0

        if len(str)==0:
            print("String is Empty")

        elif len(str)==1:
            print("Word is 1")

        else:
            
            for i in str.split():
                count+=1
            print("Count",count)

def Excute_7():
    Count_Words("")
    Count_Words("i")
    Count_Words("I Love d Python")

# Excute_7()

'''9 Remove spaces from a string.'''
def Remove_space(str):

    if len(str)==0:
        print("String is Empty")

    else:
        strs=""
        for i in str:
            if i == " ":
                str.replace(" ","")
            else:
                strs=strs+i
        print(strs)

def Excute_8():
    Remove_space("")
    Remove_space("     fataz soratpor")
# Excute_8()

'''9 Count how many times a given character appears.'''
def count_how_many_charcter(str,target):
    if len(str)==0:
        print("String is Empty")

    else:
        count=0
        if target in str:
            for i in str:
                if i in target:
                    count+=1
            print('count=',count)
        else:
            print("target are not present")
        
def Excute_9():
    count_how_many_charcter("","")
    count_how_many_charcter("","a")
    count_how_many_charcter("a","a")
    count_how_many_charcter("aaaa","a")
# Excute_9()

'''10 Find the first non repeating character.'''
def first_non_repeat(str):
    if not str:
        return "Empty"
    for i in str:
        if str.count(i)==1:
            return i
        
    return "No one"
def Excute_10():
    print(first_non_repeat(""))
    print(first_non_repeat("aabbb"))
    print(first_non_repeat("asabsbcdd"))
# Excute_10()

'''11 Find the first repeating character.'''
def first_repeat(str):
    if not str:
        return "Empty"
    for i in str:
        if str.count(i)==2:
            return i
        
    return "No one"
def Excute_11():
    print(first_repeat(""))
    print(first_repeat("aabbb"))
    print(first_repeat("asabsbcdd"))
# Excute_11()

'''12 Check whether two strings are anagrams.'''
def anagram(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    if len(str1)!=len(str2):
        return False

    return sorted(str1)==sorted(str2)
      

# a=anagram("Fayaz","zayaf")
# print(a)



'''13 Remove duplicate characters while preserving order.'''
def remove_duplicate(str):
    if len(str)==0:
        return "String is Empty"
    str2=""
    for i in str:
        if i not in str2:
            str2=str2+i
    return str2

def Excute_13():
    print(remove_duplicate("  "))
    print(remove_duplicate("a"))
    print(remove_duplicate("abc"))
    print(remove_duplicate("RRRRRRRRRRRRRRCCCCCCCCCCCCCCCCCCCBBBBBBBBBBBBBB"))

# Excute_13()


'''14 Find the most frequent character.'''
def Most_frequent_Character(str):
    if len(str)==0:
        return "String is Empty"

    most=str[0]
    for i in str:
        if str.count(i)>str.count(most):
            most=i

    return most

# print(Most_frequent_Character("aaabbbb"))

'''15 Count the frequency of every character.'''
def Frequency(str):
    if len(str)==0:
        return "Empty"
    frequency={}

    for i in str:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    return frequency
def Excute_15():
    print(Frequency(""))
    print(Frequency("a"))
    print(Frequency("aa"))
    print(Frequency("Fayaz"))

# Excute_15()

'''16 Check whether one string is a rotation of another.'''
def String_Rotation(s1,s2):


    if len(s1) != len(s2):
        return False

    return s2 in (s1 + s1)

def Excute_16():
    print(String_Rotation("abcd", "cdab"))
    print(String_Rotation("abcd", "acbd"))
    print(String_Rotation("abc", "abcd"))
    print(String_Rotation("abc","cab"))

# Excute_16()
'''17 Capitalize the first letter of every word.'''
def Capitailize(str):
    if len(str)==0:
        return "Emppty"

    return str.title()
# print(Capitailize("fayaz and malla are the bestfriend"))


'''18 Find the longest word in a sentence.'''
def Longest_word(str):
    if len(str)==0:
        return "Empty"

    long=str[0]
    for i in str.split():
        if len(i)>len(long):
            long=i
    return long

def Excute_18():
    print(Longest_word("ee sala cup namde le bsdkkkkk"))
    print(Longest_word("fayaz is the successful man in world"))

# Excute_18()

'''19 Check whether a string contains only digits.'''
def Only_digits(str):
    if len(str)==0:
        return "empty"

    for i in str:
        if i < "0" or i > "9":
            return False
    return True

print(Only_digits("1234"))


