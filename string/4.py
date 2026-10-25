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
