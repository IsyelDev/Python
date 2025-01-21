# Python es un lenguaje de programacion de tipado dinamico
x = 12

# Tipo de dato
print(type(x))

x = False

# Tipo de dato
print(type(x))

x = 12.3**(0.333)

# Tipo de dato
print(type(x))

x = "True"

# Tipo de dato
print(type(x))

x = 0

# Tipo de dato
print(type(x))


# Documentacion de la funcion isalpha
help(cad1.isalpha)

cad1 = 'Python'

"123".isalpha()

# Solucion de una ecuacion cuadratica
a = float(input("Ingrese el coeficiente cuadratico : "))
b = int(input("Ingrese el coeficiente lineal : "))
c = float(input("Ingrese el termino independiente : "))

# Operaciones
disc = b**2 - 4*a*c

# Calculo de las raices : Formula general
x1 = (-b - disc**(0.5))/(2*a)
x2 = (-b + disc**(0.5))/(2*a)

# Mostremos los resultados
print(x1)
print(x2)



# \n : SAlto de linea
# \t : tabular (4 espacios)
# %f : mostrar variables de tipo punto flotante
# %.3f : Mostremos un numero punto flotante con solo 3 cifras despues del punto decimal
# %i : Mostrar numeros enteros
# %s : mostrar variables de tipo cadena de caracter
print("Nombre : \t %s \nEdad : \t %i" %(nombre1, edad1) )


# Formateando la salida usando docstrings
print("""
  Calculo del Indice de Masa Corporal (IMC)
    Peso : %f
    Estatuta : %f
    -------------
    IMC : %.3f

"""%(peso, estatura, IMC))



# Ley de Coulomb
# Dadas dos cargas puntuales q1 y q2, la fuerza electrica entre
# estas esta dada por k*q1*q2/d**2

# Pidamos al usuario las cargas y la distancia
q1 = float(input("Ingresa q1 : "))
q2 = float(input("Ingresa q2 : "))
d =  float(input("Ingresa la distancia de separacion : "))

# Calculos
F = (9*10**9 * q1 * q2)  / (d**2)

# Mostremos los resultados
print("""
Fuerza de Coulomb
  q1 = %f
  q2 = %f
  d = %f

  Fuerza Electrica : %.2f

""" %(q1,q2, d,F))





# Calculo de areas de un triangulo
# Dados los tres lados de un triangulo , calcular su area

# Entradas de mi programa
lado_a = float(input("Ingrese el lado a : "))
lado_b = float(input("Ingrese el lado b : "))
lado_c = float(input("Ingrese el lado c : "))

# Calculos : Formula de Heron
s = (lado_a + lado_b + lado_c)/2
area = (s * (s-lado_a) * (s-lado_b) * (s-lado_c))**(0.5)

# Mostremos los resultados
print("""
Area de un triangulo (Formula de Heron)
  a : %f
  b : %f
  c : %f

  AREA : %f
""" %(lado_a, lado_b, lado_c, area))





# Generemos un par de valores aleatorios
import random as rnd
a = rnd.paretovariate(12.8)
b = rnd.paretovariate(-63.9)




# Existencia de un triangulo
l1 = float(input("Ingrese el primer lado de un triangulo : "))
l2 = float(input("Ingrese el segundo lado de un triangulo : "))
l3 = float(input("Ingrese el tercer lado de un triangulo : "))

# Carguemos el modulo math para acceder a la funcion fabs
import math as m


# Validemos que los datos del triangulo son positivos (>0)
if (l1>0) and (l2>0) and (l3>0):
  # Validemos la existencia del triangulo
  if (m.fabs(l2-l3) < l1 < l2 +l3) and (m.fabs(l1-l3)< l2 < l1+l3) and (m.fabs(l1-l2) < l3 < l1+l2) :
    print("Triangulo Existe => Calculemos su area")
  else:
    print("El triangulo  no existe ")
else:
  print("Valores INCORRECTOS")






