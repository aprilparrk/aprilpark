food = ["pizza", "salad", "pasta", "matcha", "bread"]

print(food[1])
print(food[-1])
food.append("soup")
food.insert(0, "apple")
food.remove(food[2])
print(food)
print(len(food))

for i in food:
    print(i.upper())

new_food = food[::len(food)-1]
print(new_food)

if i == "potato":
    print("A potato!")
else:
    print("No potato!")


numbers = list(range(22))

def get_first_15(list):
    return list[0:15]

def get_every_5th(list):
    return list[::5]

def reverse_and_stride(list):
    list_reversed = list[::-1]
    return list_reversed[::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)


list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = [7,8,9]

numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(numbers[2])
print(numbers[1][1])
numbers.append([10,11,12])
print(numbers[3])
def sum_nested(numbers):
    total = 0
    for row in numbers:
        total = total + sum(row)
    return total
print(sum_nested(numbers))

def make_5by5():
    fbyf = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        fbyf.append(row)
    return fbyf

def replace(fbyf):
    new = []
    for row in fbyf:
        new_row = []
        for num in row:
            if num % 3 ==0:
                new_row.append("?")
            else:
                new_row.append(num)
        new.append(new_row)
    return new

def not_question(fbyf):
    total = 0
    for row in fbyf:
        for thing in row:
            if thing != "?":
                total += thing
    return total

matrix = make_5by5()
for row in matrix:
    print(row)

updated_matrix = replace(matrix)
for row in updated_matrix:
    print(row)

sum_result = not_question(updated_matrix)




ages = {
    "Katie":30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]

for name in ages:
    print(name, ages[name])