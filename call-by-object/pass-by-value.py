#Example 1
def set_str(str1):
    print(id(str1))
    str1 = 'shirke'
    print(id(str1))    
    return str1

str1 = 'vishal'
print(id(str1))
print(set_str(str1))
print(id(str1))