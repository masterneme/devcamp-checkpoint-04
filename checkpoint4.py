# Exercise 1
from decimal import Decimal as Dec
my_list = ["Esto", "es", "1", "lista"]
#print(type(my_list))
my_tuple = ("Esto", "es", 1, "tupla")
#print(type(my_tuple))
my_float = 1.234
#print(type(my_float))
my_integer = 5
#print(type(my_integer))
my_decimal = Dec(6.789)
#print(type(my_decimal))
my_dictionary = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}
#print(type(my_dictionary))

# Exercise 2
import math
ceil_float = math.ceil(my_float)
#print(ceil_float)

# Exercise 3
root_float = math.sqrt(ceil_float)
#print(root_float)

# Exercise 4
dictionary_element = my_dictionary["clave1"]
#print(dictionary_element)

# Exercise 5
tuple_element = my_tuple[1]
#print(tuple_element)

# Exercise 6
my_list.extend(["True"])
#print(my_list)

# Exercise 7
my_list[0] = "Sustituto"
#print(my_list)

# Exercise 8
my_list.sort()
#print(my_list)

# Exercise 9
my_tuple += ("extendida",)
#print(my_tuple)