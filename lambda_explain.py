#lib mandatory
from functools import reduce

#función de palíndromo

palindrome = lambda string: string == string[::-1]

print(palindrome("ANA"))

#filter

my_list = [1,2,3,4,5,6]

odd = list(filter(lambda x: x%2 != 0,my_list))
print(odd)

#Map 
odd1 = list(map(lambda x: x%2 != 0,my_list))
print(odd1)

#Reduce 
my_list_2 =  [2,2,2,2,2,2,2]
odd2 = reduce(lambda a, b: a * b, my_list_2 != 0,my_list_2)
print(odd2)

