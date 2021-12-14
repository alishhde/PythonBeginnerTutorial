import string

strr = """They're useed after a subordinate'e clause at the start of a sentence "e" this is very hard, nadomme. che. domme."""


e_counter = 0
for i in strr:
    
    if i in string.punctuation:
        strr = strr.replace(i, " ")
    lst_str = strr.split(" ")
    
for r in lst_str:
    if "e" in r:
        e_counter += 1

print(strr)
print(lst_str)
print(e_counter)





















# words = strr.split()

# for i in words:
# #     print(i)
# e_counter = 0
# punc_counter = 0

# for i in strr:
#     if i == "e" or i == "E":
#         e_counter += 1
#     elif i in string.punctuation:
#         print(i)
#         # print(strr)
#         strr = strr.replace(i, " ")
#         # print(strr)
#         # print(new_str)
        
#         punc_counter += 1


# print(e_counter)
# print(punc_counter)
# # print(new_str)
