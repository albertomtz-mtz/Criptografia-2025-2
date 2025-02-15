'''
CRIPTOGRAFIA GRUPO: 02
SEMESTRE 2025-2
'''

alfabeto= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
           "P","Q","R","S","T","U","V","W","X","Y","Z"]

mensajeCodificado=[]
mensajeCifrado=[]
listaKey=[]
listaMensaje = []

def cifrado():

    mensaje= str(input("Ingrese su mensaje: "))
    mensaje= mensaje.replace(" ","")
    print("Mensaje sin espacios: ", mensaje, "\n")
    key= str(input("Ingrese la palabra que será la llave: "))
    longMensaje= len(mensaje)
    longKey= len(key)
    if longKey > longMensaje:
        newKey= key[:len(mensaje)] 
    else:
        partEntera= longMensaje //longKey
        partSobrante = longMensaje % longKey
        newKey = (key * partEntera) + key[:partSobrante]

    print("Llave generada: ", newKey)
    print("Longitud del mensaje: ", longMensaje, "Longitud llave: ",longKey)

    for index in range(len(mensaje)):
        if mensaje[index] in alfabeto:
            print("Letra: ", mensaje[index], "llave: ", alfabeto.index(mensaje[index]))
            mensajeCodificado.append(( alfabeto.index(mensaje[index])))
        else:
            print("ERROR: CARACTER NO DEFINIDO EN EL ALFABETO \n \n")

    for indexKey in range(len(newKey)):
        if newKey[indexKey] in alfabeto:
            print("Letra: ", newKey[indexKey], "llave: ", alfabeto.index(newKey[indexKey]))
            listaKey.append(( alfabeto.index(newKey[indexKey])))
        else:
            print("ERROR: CARACTER NO DEFINIDO EN EL ALFABETO \n \n")
    
    for indexMen in range(len(mensaje)):
        listaMensaje.append((mensajeCodificado[indexMen] + listaKey[indexMen]) % len(alfabeto))
        mensajeCifrado.append(alfabeto[listaMensaje[indexMen]])

    print(mensajeCodificado, "\n")
    print(mensajeCifrado, "\n")

def descifrado():

    mensaje= str(input("Ingrese el mensaje que quiere descifrar: "))
    mensaje= mensaje.replace(" ","")
    print("Mensaje sin espacios: ", mensaje, "\n")
    key= str(input("Ingrese la palabra que es la llave: "))
    longMensaje= len(mensaje)
    longKey= len(key)
    if longKey > longMensaje:
        newKey= key[:len(mensaje)] 
    else:
        partEntera= longMensaje //longKey
        partSobrante = longMensaje % longKey
        newKey = (key * partEntera) + key[:partSobrante]

    print("Llave generada: ", newKey)
    print("Longitud del mensaje: ", longMensaje, "Longitud llave: ",longKey)

    for index in range(len(mensaje)):
        if mensaje[index] in alfabeto:
            print("Letra: ", mensaje[index], "llave: ", alfabeto.index(mensaje[index]))
            mensajeCodificado.append(( alfabeto.index(mensaje[index])))
        else:
            print("ERROR: CARACTER NO DEFINIDO EN EL ALFABETO \n \n")

    for indexKey in range(len(newKey)):
        if newKey[indexKey] in alfabeto:
            print("Letra: ", newKey[indexKey], "llave: ", alfabeto.index(newKey[indexKey]))
            listaKey.append(( alfabeto.index(newKey[indexKey])))
        else:
            print("ERROR: CARACTER NO DEFINIDO EN EL ALFABETO \n \n")
    
    for indexMen in range(len(mensaje)):
        listaMensaje.append((mensajeCodificado[indexMen] - listaKey[indexMen]) % len(alfabeto))
        mensajeCifrado.append(alfabeto[listaMensaje[indexMen]])

    print(mensajeCodificado, "\n")
    print(mensajeCifrado, "\n")

def menu():
    opcion=0
    while opcion != 3:
        mensajeCodificado.clear()
        mensajeCifrado.clear()
        listaKey.clear()
        listaMensaje.clear()
        
        print("----CIFRADO VIGENERE---- \n")
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
print(mensajeCifrado)


