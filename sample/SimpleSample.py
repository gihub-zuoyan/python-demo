import sys
import random
import sample.advanced.MyModule as my

print("start try ...")
try:
    int("w2")
except ValueError as err:
    print("except error")
    print("except error: ", err)
finally:
    print("finally error")

print("end try.....")
my.my_print("end ... try ....except ...finally ...")
my.my_print(sys.argv)
print(random.randint(1, 100))
print(random.choice(["apple", "orange", "banana"]))
print("dir()=", dir())
builtinsList = dir(__builtins__)
length = 0
for ins in builtinsList:
    length += 1
    if length / 3 == 0:
        length = 0;

    print(ins)


print("dir(__builtnins__)=", dir(__builtins__))

var_tuple = ((1, 9), (2, 8), (3, 7), (4, 6), (5, 5))
for x in var_tuple:
    print(x[0], x[1])

##========================================================
for i in range(0, 10):
    oneLine = []
    for j in range(0, i + 1):
        oneLine.append("{0} * {1} = {2}".format(j, i, i * j))
    print(oneLine)

##=========================================================
#set
var_set = {}
var_set = {1, 2, 3, 4, 5}
for x in var_set :
    print(x)

var_dict = {"time":1, "second": 2, "third": 3}
for _ in var_dict.items() :
    print(_[0], _[1], type(_))

for line in open("SimpleSample.py", encoding="utf-8"):
    print(line)

