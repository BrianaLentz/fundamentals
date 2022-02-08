from ast import Add


for x in range(151):
    print(x)

print("*"*5)

total = 5
while total <= 1000:
    print(total)
    total = total + 5



for i in range (1,101):
    
    if i % 10 ==0:
        print ('Coding Dojo')
    if i % 5 ==0:
        print ('Coding')
    else:
        print(i)
    
print("*"*5)

def add_int():
    sum = 0
    for i in range(500001):
        if i %2 ==1:
            sum = sum + i
    return sum
print(add_int())

def add_num():
    sum = 0
    for i in range(1, 500001, 2):
        sum = sum + i
    return sum
print(add_num())

print("*"*5)

for i in range(2018, 0, -4):
    print(i)

print("*"*5)

def numbers(low_num, high_num, mult):
    for i in range(low_num,high_num+1):
        if i % mult ==0:
            print(i)
numbers(1,20,4)
