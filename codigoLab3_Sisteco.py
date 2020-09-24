# -*- coding: utf-8 -*-
# IMPORTACION DE BIBLIOTECAS    
from Crypto.Cipher import AES
import base64

# DEFINICION DE FUNCIONES

#ENTRADA: Mensaje a Encriptar, Llave para encriptar y alfabeto de uso Cesar
#SALIDA: Se Obtiene la Encriptacion mixta de una mensaje (Mixta = Cesar + Cypher) 
#FUNCIONAMIENTO: 
def encriptacionCesar(mensaje, llave,alfabeto):
    llaveCesar = len(llave)
    contadorEspacios = llave.count(" ")
    contadorLetras = len(llave)-contadorEspacios
    largoLlave = len(llave)
    llaveAES = str(llave[largoLlave-1])+str(contadorEspacios*contadorLetras*largoLlave)+str(llave[0])
    largoLlaveAES = len(llaveAES)
    for i in range(largoLlaveAES, 16):
        llaveAES = llaveAES+'1'
    obj = AES.new(llaveAES, AES.MODE_CBC, llaveAES[::-1])

    #Encriptacion Cesar
    mensaje = mensaje.upper()
    encripCesar = ""
    for caracter in mensaje:
        if caracter in alfabeto:
            pos = alfabeto.find(caracter)
            pos = pos + llaveCesar
            if pos >= len(alfabeto):
                pos = pos - len(alfabeto)
            elif pos < 0:
                pos = pos + len(alfabeto)
            encripCesar = encripCesar + alfabeto[pos]
        else:
            encripCesar = encripCesar - caracter

    #Encriptacion Cipher
    encrip = obj.encrypt(encripCesar)
    encrip = base64.b64encode(encrip).decode()
    print("Mensaje Cifrado: "+str(encrip))
    return encrip

#ENTRADA: Mensaje a Desencriptar, Llave para Desencriptar y alfabeto de uso Cesar
#SALIDA: Se Obtiene la Desencriptacion mixta de una mensaje (Mixta = Cesar + Cypher)
#FUNCIONAMIENTO:
def desencriptacionCesar(mensaje, llave,alfabeto):
    mensaje = "K3E6k/M1P8yJcfHEOj+4wg=="

    llaveCesar = len(llave)
    contadorEspacios = llave.count(" ")
    contadorLetras = len(llave)-contadorEspacios
    largoLlave = len(llave)
    llaveAES = str(llave[largoLlave-1])+str(contadorEspacios*contadorLetras*largoLlave)+str(llave[0])
    largoLlaveAES = len(llaveAES)
    for i in range(largoLlaveAES, 16):
        llaveAES = llaveAES+'1'
    obj = AES.new(llaveAES, AES.MODE_CBC, llaveAES[::-1])

    #Desencriptacion Cypher
    mensaje = mensaje.encode()
    encodeMensaje = base64.b64decode(mensaje)
    newMensaje = obj.decrypt(encodeMensaje).decode()

    #Desencriptacion Cesar
    desencripCesar = ""
    for caracter in newMensaje:
        if caracter in alfabeto:
            pos = alfabeto.find(caracter)
            pos = pos - llaveCesar
            if pos >= len(alfabeto):
                pos = pos - len(alfabeto)
            elif pos < 0:
                pos = pos + len(alfabeto)
            desencripCesar = desencripCesar + alfabeto[pos]
        else:
            desencripCesar = desencripCesar - caracter
    print("Mensaje Descifrado: "+desencripCesar)
    return desencripCesar


# ENTRADA: mensaje a encriptar,llave para usar en el tipo de encriptado y modo de encriptacion.
# SALIDA: Retorno de Mensaje cifrado o descifrado.
# FUNCIONAMIENTO: Esta funcion referencia el alfabeto cesar y dependiendo del modo de Cifrar o descifra llama a la funcion respectiva
def encriptacionMixta(mensaje, llave, modo):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
    # Encryptar mensaje
    if modo == 1:
        encriptacionCesar(mensaje, llave,alfabeto)

    # Desencryptar mensaje
    elif modo == 2:
        desencriptacionCesar(mensaje, llave, alfabeto)
        
# BLOQUE PRINCIPAL 
def main():
    modo    = int(input("Modo de Encriptacion \n #Cifrar = 1 \n #Descifrar = 2 \n\n Ingrese numero: "))
    mensaje = input("Introducir Mensaje a Encryptar en letras: ")
    llave   = str(input("Ingrese Llave en letras y numeros: "))
    criptado = str(encriptacionMixta(mensaje, llave, modo))
        

# LLAMADO DE FUNCIONES
main()







