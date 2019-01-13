
# code to check if the strings are anagrams
# assumption is made that all the letters are used only once.
from operator import xor

string1 = "Adultery"
string2 = "true lad"
res1 = 1
for a in string1.lower():
    if a != " ":
        res1 = xor(res1, ord(a))

res2 = 1
for a in string2.lower():
    if a != " ":
        res2 = xor(res2, ord(a))

if res1 == res2:
    print "String is an anagram"
else:
    print "String is not anagram"



# arr = []
# arr2 = []
# for c in string1:
#     if c != " ":
#        arr.append(ord(c))
#
# for c in string2:
#     if c != " ":
#         arr2.append(ord(c))
#
# res1 = 1
# for a in arr:
#     res1 = xor(res1, a)
#
# res2 = 1
# for a in arr2:
#     res2 = xor(res2, a)

