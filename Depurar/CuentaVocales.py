def vocales(palabra):
    vocales = "aeiouáéíóúAEIOU"
    Contador = 0
    for letra in palabra:
        if letra in vocales:
            Contador += 1
    return Contador

print("")
palabra = input("Ingrese una palabra: ")
print("")
print("Numero de vocales: ", vocales(palabra))
print("") 