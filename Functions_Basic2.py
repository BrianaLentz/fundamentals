# Question1
def countdown(num):
    numbers = []
    for i in range(num, -1, -1):
        numbers.append(i)
    # [8,7,6,5,4,3,2,1,0]
    return numbers
print(countdown(8))

# Question2
def print_return(num):
    print(num[0])
    return num[1]
print (print_return([3,5]))

# Question3
def f_plus_l(sum):
    sum = sum[0] + len(sum)
    return sum
print(f_plus_l([12,34,56,78]))

print("*")

# Question4
def values_greater_than_second(list):
    if len(list)<2:
        return False
    new_list = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            new_list.append(list[i])
    print(len(new_list))
    return new_list
print(values_greater_than_second([7,2,4,2,6,5]))
print(values_greater_than_second([4]))


print("***")

# Question5
def l_and_v(size,value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list
print(l_and_v(4,30))