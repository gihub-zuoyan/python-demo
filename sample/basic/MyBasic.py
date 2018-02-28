var_int = 12
print("hello", "world")
print("num =", var_int)
print("0123456789"[8])
print("abcdefghijklmn"[9])
var_int = int("12")
#print var_int value
print("var_int=", str(var_int)) #print var_int
print(var_int, type(var_int))
var_int = "var_int"
print(var_int, type(var_int))
#tuple
var_tuple = ()
print(var_tuple, type(var_tuple))
var_tuple = ("first", "second", "third")
print(var_tuple)
#list
var_list = [];
print(var_list, type(var_list))
var_list = ["list1", "list2"]
print(var_list, type(var_list))
var_list = ["list0", 1234, 2334, "list2"]
print(var_list, len(var_list), type(var_list))
var_list = [];
var_list.append("hello")
print(var_list, len(var_list), type(var_list))
list.append(var_list, "second")
print(var_list, len(var_list), type(var_list))
print(var_list[len(var_list) -1])
var_list[len(var_list) -1 ] = "second_modify"
print(var_list[len(var_list) -1])
print( var_int is var_list)
var_bool = None
print(var_bool)
print("hello" in var_list)
print("hello" not in var_list)
