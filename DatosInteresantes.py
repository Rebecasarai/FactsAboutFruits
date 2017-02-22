# -*- coding: utf-8 -*-
# !/usr/bin/python

from pip._vendor.distlib.compat import raw_input


class Frutas:
    counter = 0

    def __init__(self, namefru, datos):
        self.namefru = namefru
        self.datos = datos
        Frutas.counter += 1

    def displayCount(self):
        print("Número de datos de frutas en nuestra base: %d" % Frutas.counter)

    def displayFruit(self):
        print("¿Sabias de las ", self.namefru, " que ", self.datos, "?\n")

manzana1 = Frutas("Manzanas", "la ciencia del cultivo de la manzana se llama pomología")
"This would create the fruits"
pera1 = Frutas("Peras", "en China son consideradas como un símbolo de longevidad")
kiwi1 = Frutas("Kiwis", "contiene dos veces más vitamina C que la naranja y el doble de vitamina E que el aguacate.")
sandia1 = Frutas("Sandia", " es 92% agua")


print(30 * '-')
print("   ¿Quieres saber datos interesantes de las frutas?")
print(30 * '-')
print("1. Sí")
print("2. Tal vez")
print("3. No.")
print(30 * '-')

## Get input ###
choice = raw_input('Elije una opción [1-3] : ')

### Convert string to int type ##
choice = int(choice)

### Take action as per selected menu-option ###
if choice == 1:
    print("¡Vamos!\n")

    cad = raw_input('Escribe tu fruta favorita')
    if cad.upper()=='MANZANA':
        manzana1.displayFruit()
    elif cad.upper()=='PERA':
        pera1.displayFruit()
    elif cad.upper()=='KIWI':
        kiwi1.displayFruit()
    elif cad.upper()=='SANDIA':
        sandia1.displayFruit()




elif choice == 2:
    cad = raw_input('Entiendo, a veces las decisiones son dificiles. Escribe tu fruta favorita')

    if cad.upper()=='MANZANA':
        manzana1.displayFruit()
    elif cad.upper()=='PERA':
        pera1.displayFruit()
    elif cad.upper()=='KIWI':
        kiwi1.displayFruit()
    elif cad.upper()=='SANDIA':
        sandia1.displayFruit()


elif choice == 3:
    print("¿No?")
    razon = raw_input("¿Por qué no?")
    if(razon != "es verdad, no tengo razón"):
        print("Razón no valida, así que mira de todas maneras:\n")
        sandia1.displayFruit()
        manzana1.displayFruit()
        pera1.displayFruit()
        kiwi1.displayFruit()

else:  ## default ##
    print("Opción invalida, por favor introduzca de nuevo.")




print("Número total de frutas en nuestra base hasta el momento: %d" % Frutas.counter)

print(30 * '-')
print("   ¿Te ha gustado la app?")
print(30 * '-')
print("1. Sí")
print("2. Algo")
print("3. No.")
print(30 * '-')

## Get input ###
choice = raw_input('¿Cuál eliges? [1-3] : ')

### Convert string to int type ##
choice = int(choice)

### Take action as per selected menu-option ###
if choice == 1:
    print("¡Me alegro!\n")

elif choice == 2:
    print("¡El mundo de las frutas es interesante! \n")
elif choice == 3:
    print("¿No?")
    razon = raw_input("¿Por qué no?")

    if (razon != "es verdad, no tengo razón"):
        print("Razón no valida, así que deberías ir a comerte una.\n")
else:  ## default ##
    print("Opción invalida, por favor introduzca de nuevo.")


