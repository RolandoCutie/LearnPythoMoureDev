
#### Trabajo con listas#####

# Formas de declarar una lista
my_list = list()
my_other_list = []

# ingresando valores a una lista
my_other_list = [1, 2, 3, "34"]

print(len(my_list))
print(len(my_other_list))


#Trabajando con la listas
#A;adimos valres a la lista en su ultima posicion
my_other_list.append("Hola")

#Insertamos valores en la lista en la posicion deseada
my_other_list.insert(0, "Hola Mundo")

#Eliminamos la primera ocurrencia que haya en la lista con un valor dado
my_other_list.remove("Hola")


#Obtenemos el ultimo valor de la lista y el indice de ese valor y ademas lo sacamos e la lista
print(my_other_list.pop())
v=my_other_list.pop()
print(v)


