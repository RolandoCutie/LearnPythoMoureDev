# Variables
my_string_variable = "Variable"
print(my_string_variable)

# Variable entera
my_int_variable = 34
print(my_int_variable)

# Variable boleana
my_boolean_variable = True
print(my_boolean_variable)

pow(my_boolean_variable)


# Convirtiendo variable int en string
my_int_variable_to_str_variable = str(my_int_variable)
print(my_int_variable_to_str_variable)

# Consultando tipop de datos
print(type(my_int_variable_to_str_variable))


# Concatenacion de varibales en un print
print(my_string_variable, my_int_variable_to_str_variable, my_boolean_variable)


# Funciones del sistema
print("La variable tiene una longuitud de :", len(my_string_variable))


# Variables en una sola linea
name, surname, alias, age = "Rolando", "Garcia", "Roly", "31"

print("Me llamo:", name, "Mi apellido es:", surname,
      "Mi alias es:", alias, "Mi edad es", age)

# Cambiando el tipo de la variable my_int_variable
my_string_variable = "46"
print(my_string_variable)


# Estableciendo una variable el tipo para no tener que perder su tipo en caso de que se cambie el vaor
adress: str = "Calle 20"
adress = 20

