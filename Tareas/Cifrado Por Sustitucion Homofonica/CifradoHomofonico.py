import random

mensajeCifrado= []
mensajeDescifrado=[]

abecedario = {
    'A': ['00001110', '01010111', '11001000', '00101101', '00001001'],
    'B': ['00011111', '10011010', '11011100'],
    'C': ['00111010', '01101110', '11001001'],
    'D': ['01010100', '00000011', '10101010'],
    'E': ['00010111', '01001100', '10000001', '11011110', '00000001'],
    'F': ['01000011', '01110110', '11110000'],
    'G': ['00100001', '11000001', '10001101'],
    'H': ['01100011', '11010000', '00000110'],
    'I': ['01000111', '01100110', '10111001', '00100111', '00001100'],
    'J': ['11000110', '01010010', '00001111'],
    'K': ['00110000', '11010100', '01101001'],
    'L': ['11000010', '00001000', '10000010'],
    'M': ['00011001', '10101101', '10010000'],
    'N': ['10100101', '11010101', '00000101'],
    'O': ['00101011', '10111110', '01001110', '11110001', '00000010'],
    'P': ['01100001', '10000111', '00100000'],
    'Q': ['01000010', '10011110', '11010011'],
    'R': ['00110111', '00001010', '11000000', '01001000', '10100011'],
    'S': ['01100101', '00010101', '11011111', '00010001', '10111101'],
    'T': ['10010101', '01101111', '00100110'],
    'U': ['11001111', '01010011', '10001110'],
    'V': ['01100000', '00111101', '11011001'],
    'W': ['10101001', '00101100', '10011100'],
    'X': ['01001011', '00010011', '11111000'],
    'Y': ['11100010', '00001101', '10011000'],
    'Z': ['01101000', '00100010', '11100101']
}

def cifradoHomofonico():
    bandera =0
    mensaje= str(input("Ingrese su mensaje: "))
    mensaje= mensaje.replace(" ","")
    print("Mensaje sin espacios: ", mensaje, "\n")
    for index in range(len(mensaje)):
            bandera = 0
            if mensaje[index] in abecedario:
                  llaves = abecedario[mensaje[index]]
                  limSup = len(llaves)-1
                  #print("LETRA EVALUDA: ", mensaje[index], "POSIBLES LLAVES: ", llaves, "Longitud: ", limSup, "\n")
                  keyVal= random.randint(0, limSup)
                  mensajeCifrado.append(llaves[keyVal])
                  bandera =1
            else:
                  print("EL MENSAJE TIENE UN CARCTER NO ESTABLECIDO EN EL ABECEDARIO\n\n")
                  break
    if bandera == 1:  
        print("SU MENSAJE CIFRADO ES: ", mensajeCifrado, "'\n\n")
    else:
         print("ERROR EN EL CIFRADO")

def descifradoHomofonico():
    bandera= 0
    mensaje= str(input("Ingrese su mensaje: "))
    mensaje= mensaje.replace(" ","")
    ####cadena = "Esta es una cadena de texto muy larga que quiero dividir"

    # Crear una lista de fragmentos de 8 caracteres
    fragmentos = [mensaje[i:i+8] for i in range(0, len(mensaje), 8)]
    for fragmento in fragmentos:
        bandera = 0
        for letra in abecedario.keys():
            if fragmento in abecedario[letra]:
                 mensajeDescifrado.append(letra)
                 bandera =1 
                 break
        if bandera == 0:
             print("ERROR. LA LLAVE: ", fragmento, "NO SE ENCUENTRA\n")
             break
    if bandera== 0:
         print("ERROR\n\n")
    else:     
        print("SU MENSAJE DESCIFRADO ES: ", mensajeDescifrado, "\n")

        

def menu():
    opcion=0
    while opcion != 3:
        mensajeDescifrado.clear()
        mensajeCifrado.clear()

        print("----CIFRADO HOMOFONICO---- \n")
        print("1) Cifrar un mensaje \n")
        print("2) Dsecifrar un mensaje \n")
        print("3) SALIR")
        opcion = int(input("Opcion: "))
        if opcion == 1:
             cifradoHomofonico()
        else:
            if opcion == 2:
                descifradoHomofonico()
            else:
                if opcion == 3:
                    print("GRACIAS POR USAR EL CIFRADO HOMOFONICO \n")
                else:
                    print("Opcion no valida. Intente con un valor definido \n")



menu()
