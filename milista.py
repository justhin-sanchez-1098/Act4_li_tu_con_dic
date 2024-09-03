# ejemplo de uso de listas
misnovias = ["daniela", "mariana", "zoe"]
misnumeros = ["10", "7", "11"]

#mostrando mis novias
print(misnovias)

#mostrando mis numeros
print(misnumeros)

print("")
print("--- accediendo a los elementos de la lista ---")
print(misnovias[1])


print("")
if "zoe" in misnovias:
    print("si,'zoe' esta en la lista de mis novias")
else:
    print("chale no eres mi novia")
    print("numero de novias")

print("")
Nnovias = len(misnovias)
print(f"numero de novias {Nnovias}")
print("ciclo for en las listas")
posicion=0
for medianaranja in misnovias:
    print(posicion," ",medianaranja)
    posicion=posicion+1