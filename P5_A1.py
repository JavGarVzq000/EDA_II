import random 
import string  

def formaArreglo(tamano):
    Arr = [None] * tamano
    return Arr

def obtenerLlaveNumerica(llave):
    hash = 0
    for char in str(llave):
        hash += ord(char)
    return hash

def H(llaveN):
    return llaveN % 5

def agregar(llave, valor, map, tamano):
    llave_hash = H(obtenerLlaveNumerica(llave))
    ParllaveValor = [llave, valor]
    if map[llave_hash] is None:
        map[llave_hash] = list([ParllaveValor])
        return True
    else:
        for par in map[llave_hash]:
            if par[0] == llave:
                par[1] = valor
                return True
        for j in range(tamano):
            llaveh = (llave_hash + j) % 13
            if (llaveh == len(map)):
                print("Tabla llena", llave_hash)
                break
            else:
                if map[llaveh] is None:
                    map[llaveh] = list([ParllaveValor])
                    return True
                
def buscar(llave, map, tamano):
    llave_hash = H(obtenerLlaveNumerica(llave))
    if map[llave_hash] is not None:
        for par in map[llave_hash]:
            if par[0] == llave:
                return par[1]
            else:
                for j in range(tamano):
                    llaveh = (llave_hash + j) % 13
                    if (llaveh == len(map)):
                        break
                    for par1 in map[llaveh]:
                        if par1[0] == llave:
                            return par1[1]
    return None

def valores(num, map, tamano):
    for i in range(num): #se va a encargar de crear el numero de valores que ingreso el usuario
        longitudCadena = 15#el tamannio que tendra la cadena de caracteres
        letras = string.ascii_letters#string.ascii_letters duvuelve el abecedario en mayusculas y minusculas
        digitos = string.digits#string.digits devuelve los numeros del 0 al 9
        alfanumerico = letras + digitos#junta el abecedario y los numeros
        llaveCreada = ""#se crea una variable que guardara la llave 
        for i in range(longitudCadena):
            #random.choice escogera aleatoriamente un caracter que este en alfanumerico
            #''.join se encargara de formar una cadena de caracteres y se guarda en la variable llaveCreada
            llaveCreada += ''.join(random.choice(alfanumerico))
        llave = str(llaveCreada)#se asegura que llaveCreada sea de tipo String
        clave = random.randint(10e6, 10e8)#se genera un numero aleatorio
        agregar(llave, clave, map, tamano)#se llama a la funcion agregar

#main
ban = False
bandera = False

while not ban:
    print("--------------------------------------------------------------")
    numValores = int(input("Ingrese el numero de datos a crear: "))
    if (numValores > 5):
        map = formaArreglo(numValores)
        tam = len(map)
        valores(numValores, map, tam)
        ban = True

while not bandera:
    print("--------------------------Tabla Hash--------------------------")
    for x in map:
        print(x)
    print("---------------------------Opciones---------------------------")
    print("1.- Buscar")
    print("2.- Salir")
    opcion = int(input("Ingrese la opcion que desea: "))
    if opcion == 1:
        print("--------------------------------------------------------------")
        clave = str(input("Ingrese el valor a buscar:"))
        print(f"--La llave de {clave} es: {buscar(clave, map, tam)}")
        bandera = False
    else:
        print("--------------------------------------------------------------\n")
        bandera = True