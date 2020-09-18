


# DEFINICION DE FUNCIONES



# ENTRADA: mensaje a encriptar,llave para usar en el tipo de encriptado y modo de encriptacion.
# SALIDA: Retorno de Mensaje cifrado o descifrado.
# FUNCIONAMIENTO: Se realiza la funcion de encriptacion de un mensaje con el cifrado de tipo cesar, pero se le agrega una modificacion
#                 donde el largo de la llave ingresada, define la cantidad de desplazamiento del cifrado cesar en el alfabeto
def encriptacionCesar(mensaje, llave, modo):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
    mensaje  = mensaje.upper()
    llave = len(llave)  
    encrip = ""
    for caracter in mensaje:
        if caracter in alfabeto:
            pos = alfabeto.find(caracter)
            if modo == 1:
                pos = pos + llave
            elif modo == 2:
                pos = pos - llave
            if pos >= len(alfabeto):
                pos = pos - len(alfabeto)
            elif pos < 0:
                pos = pos + len(alfabeto)
            encrip = encrip + alfabeto[pos]
        else:
            encrip = encrip - caracter
    return encrip

# BLOQUE PRINCIPAL 
def main():
    mensaje = input("Introducir Mensaje en letras: ")
    llave   = str(input("Ingrese Llave en letras y numeros: "))
    modo    = int(input("Modo de Encriptacion \n #Cifrar = 1 \n #Descifrar = 2 \n\n Ingrese numero: "))
    criptado = encriptacionCesar(mensaje, llave, modo)
    if modo ==  1:
        print("Mensaje Cifrado: "+criptado)
    elif modo == 2:
        print("Mensaje Descifrado: "+criptado)

# LLAMADO DE FUNCIONES
main()
