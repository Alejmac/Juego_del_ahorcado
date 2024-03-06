from random import choice
from os import system
def generarletra():
    frutas = ['pera', 'manzana', 'platano', 'ciruela']
    letra = choice(frutas)
    #pprint(letra)
    return letra
def ingresarletra():
    print("*"*50)
    letra = str(input("ingresa una letra\n "))
    return letra

def validar_letra(letra_Correcta,letra_Usuario):
    #print(letra_Usuario)
    apro=" "
    #creo la palabra en una lista
    temporal1=[n for n in letra_Correcta]
    print(temporal1)
    #buscar si a letra del usuario es la misma que una de la lista
    for i in temporal1:
        if letra_Usuario in  temporal1:
                apro = letra_Usuario
                print(f" la letra que ingreso es : {apro}")
                return apro
    print(f"no le atinaste con la {letra_Usuario}, sigue intentando......\n ")
    return False


def play ():
    vidas = 6
    resultado = []
    #generar letra random
    Letra_Random= generarletra()
    print(Letra_Random)
    while vidas >=1 :
        #ingresa el ususario
        print(f"las letras son {resultado}")
        play1 = ingresarletra()
        #creamos la validacion
        validar = validar_letra(Letra_Random,play1)
        print(f" el resultao de validar es {validar}")
        if validar != False:
             system('cls')
             print("si le atinaste ")
             resultado.append(validar)

        else:
            system('cls')
            print("sigue intentando .....")
            if vidas>0:
                vidas -= 1
                print(f"te quedan :{vidas} vidas en total ... sigue participando ")
            else:
                print(f"te  :{vidas} vidas en total ... ultimo intendo")
        if len(resultado) == len(Letra_Random):
            print(f"felicidades has ganado con  {vidas} vidas ")
            break

    print("se te terminaron las vidas ..... adios")


play()

