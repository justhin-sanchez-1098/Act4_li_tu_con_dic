arcoiris=("azul", "verde", "rojo", "amarillo")
print(arcoiris)
print("-longitud arcoiris--")
print(len(arcoiris))

animales=("pantera",20,"estatura",1.7)
print(animales)
print("-elementos de la tupla-")
print(animales[2])
rateros = ("juan", "ana", "pedro")
y = list(rateros)
y[1] = "polainas"
x = tuple(y) 
print(x)
print("agregando elementos")
Nanimal = ("boby", "chetos")
y = list(Nanimal)
y.append("tontolin")
otratupla  = tuple(y)

print(otratupla)
print("uso de for en tuplas")
for elcolor in arcoiris:
    print(elcolor)