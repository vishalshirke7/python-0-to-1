#Example 1
def set_list(list1):
    print(id(list1))
    list1.append(["A", "B", "C"])
    print(id(list1))    
    return list1

def add(list):
    list.append("D")
    return list

my_list = ["E"]
print(id(my_list))
print(set_list(my_list))
print(id(my_list))
print(add(my_list))