# 1.
from multiprocessing.sharedctypes import Value


x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

# 2.
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for dict in some_list:
        for key, val in dict.items():
            print(key, " = ", val)

    #     student["first_name"]
    #     print(student["first_name"])

    # some_list = {}
    
        # some_list = 
iterateDictionary(students)


print("*"* 20)
# 3.
students = [
        {'first_name' : 'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#name = {'first_name' : 'John', 'last_name' : 'Rosales'}
#print(name['first_name'])

def iterate_dictionary2(name, list):
 #   print(name) #'first_name
  #  print(list) #
    for dict in students:
        print(dict[name])
iterate_dictionary2('first_name', students) 
print("*"*20)
# 4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print()
def print_info(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key)
        # i need a loop that goes through all the values then print them individualy 
        # create loop
        # make variable called value in loop
        # tell the loop what list to loop through
        for value in some_dict[key]:
            print(value)
        
        
print_info(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


