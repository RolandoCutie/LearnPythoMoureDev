# Trabajo con Strings

my_string = "Hola Mundo"
my_other_string = "Hola Mundo desde otro string"

# Para saber la cantidad de caracteres que tiene un string
print(len(my_string))
print(len(my_other_string))

# Concatenando dos strings
print(my_string + " " + my_other_string)

# Probando el salto de line en los strings
print("Vamo a hacer un salto de linea aqui \n Hola")

# Probando un string con tabulacion
print("Vamos a hacer una tabulacion aqui \t dd")


# Probando formateo de variables
name, surname, age = "Rolando", "Garcia", 31
print("Mi nombre es %s,  mi apellido es %s, Mi edad es %d" %
      (name, surname, age))

# Interpolacion de datos
print(f"Mi nombre es {name}, mi apellido es {surname}, mi edad es {age}")


# Desempaquetado de caracteres
a, b, c, d, e, f = "python"
print(a)
print(b)

# Division de caracteres
# Aqui nos quedmos con los caracteres que esten entre la posicion 1 y la posicion 3
languaje_slice = "python"[1:3]

print(languaje_slice)

# Reverse
reverse_languaje = name[::-1]
print(reverse_languaje)

# Funciones para formateo de strings
print(name.capitalize())
print(name.upper())
print(name.count('n'))
print(name.isnumeric())  # Devuelve true si solo hay caracteres numericos
print(name.lower())
print(name.lower().isupper())
print(name.startswith("Ro")) # Devuelve true si la palabra comienza con esa secuencia de string


