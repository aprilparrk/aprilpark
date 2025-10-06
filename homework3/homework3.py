def say_goodbye(name):
    print("Goodbye," , name)

def circle_area(radius):
    print(3.14 * radius**2)

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a/b

def wear(temperatures):
    return(min(temperatures), max(temperatures))

def is_weekday(int):
    if int == 6 or int == 7:
        return True
    else:
        return False
    
def fuel_efficiency(distance, fuel):
    return(distance/fuel)

def secret_code(num):
    last_num = num % 10
    rest_num = num // 10
    return int(str(last_num) + str(rest_num))

def power(x, y):
    output = 1
    for i in range(0, y):
        output = output * x
    return output


def for_min(list):
    min = 10000000
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
    return min

def for_max(list):
    max = -10000000
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max

def whl_min(list):
    min = 100000
    i = 0
    while len(list) > i:
        if list[i] < min:
            min = list[i]
        i += 1
    return min

def whl_max(list):
    max = -100000
    i = 0
    while len(list) > i:
        if list[i] > max:
            max = list[i]
        i += 1
    return max

def sum(num):
    total = 0
    while num > 0:
        total += num % 10 
        num = num // 10
    return total
number = 56789
result = secret_code(number)
print(f"The result of the Secret Code with number = {number} is {result}")



