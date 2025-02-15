'''
CRIPTOGRAFIA GRUPO: 02
SEMESTRE 2025-2
'''


alfabeto= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
           "P","Q","R","S","T","U","V","W","X","Y","Z"]

mensajeCodificado=[]
mensajeCifrado=[]


def cifrado():
    mensaje= input("Ingresa el mensaje que quieres cifrar: ")
    print("Tu mensaje: ", mensaje)
    key= int(input("Ingrese un valor para su llave: "))
    for index in range(len(mensaje)):
            if mensaje[index] in alfabeto:
                print("Letra: ", mensaje[index], "llave: ", alfabeto.index(mensaje[index]))
                mensajeCodificado.append(( alfabeto.index(mensaje[index])+key) % len (alfabeto))
            else:
                 print("ERROR: CARACTER NO DEFINIDO EN EL ALFABETO \n \n")
    
    for indexM in range (len(mensajeCodificado)):
         mensajeCifrado.append(alfabeto[mensajeCodificado[indexM]])
    
    print(mensajeCodificado, "\n")
    print(mensajeCifrado, "\n")

def descifrado():
    mensajeD= input("Ingrese el mensaje que desea descifrar: ")
    print("Tu mensaje: ", mensajeD, "\n")
    key = int(input("Ingrese el valor de su llave: "))

    for index in range(len(mensajeD)):
        if mensajeD[index] in alfabeto:
            print("Letra: ", mensajeD[index], "llave: ", alfabeto.index(mensajeD[index]))
            mensajeCodificado.append(( alfabeto.index(mensajeD[index])-key) % len (alfabeto))
        else:
            print("ERROR: CARACTER NO DEFINIDO EN EL ALFABETO \n \n")
    
    for indexM in range (len(mensajeCodificado)):
         mensajeCifrado.append(alfabeto[mensajeCodificado[indexM]])

    print(mensajeCodificado, "\n")
    print(mensajeCifrado, "\n")



def menu():
    opcion=0
    while opcion != 3:
        mensajeCodificado.clear()
        mensajeCifrado.clear()
        
        print("----CIFRADO CESAR---- \n")
        print("1) Cifrar un mensaje \n")
        print("2) Dsecifrar un mensaje \n")
        print("3) SALIR")
        opcion = int(input("Opcion: "))
        if opcion == 1:
             cifrado()
        else:
            if opcion == 2:
                descifrado()
            else:
                if opcion == 3:
                    print("GRACIAS POR USAR EL CIFRADO CESAR \n")
                else:
                    print("Opcion no valida. Intente con un valor definido \n")

     
menu()
