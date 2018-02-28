# function set ================
# add function
def add(x, y):
    sum = 0
    if type(x) in (tuple, list):
        for num in x:
            sum += num
    else:
        sum += x

    if type(y) is tuple or type(y) is list:
        for num in y:
            sum += num

    else:
        sum += y

    return sum

#function max
def max(x, y):
    if x > y:
        print("x is bigger more then y")
        return x
    elif x == y:
        print("x equals y")
        return x
    else:
        print("x is smaller than y")
        return y

#sum 1..num
def sum(num):
    sum = 0
    i = 0
    while i <= num:
        sum += i
        i += 1

    return sum

def readInt():
    while True:
        varInt = input("Please input integer, like 10:")
        try:
            varInt = int(varInt)
            break
        except ValueError as err:
            print(err)
            print(varInt, "is not a integer, please input again")

    return varInt

# ==============================
int_result = add(10, 20)
print("result", int_result)
print("result", add((12, 23), 20))
print("result", add([29, 20], (10, 39)))
print("result", max(12, 30))
print("sum(100)=", sum(100))
print("int is ", readInt())