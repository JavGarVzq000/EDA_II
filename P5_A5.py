def formaArreglo(tamano):
    Arr=[None]*tamano
    return Arr

def obtenerLlaveNumerica(llave):
    hash=0
    for char in str(llave):
        hash+=ord(char)
    return hash

def H(llaveN):
    return llaveN%5

#Se tienen que guardar en una tabla Hash con tamaño fijo, y si ya se coloco en una posicion un dato-par en la posicion que deberia otro,
#entonces tenemos que almacenarlo en la siguiente posicion. Y asi sucesivamente.
def agregar(llave,valor,map,tamano):
    llave_num = obtenerLlaveNumerica(llave)
    ParllaveValor = [llave, valor]
    for i in range(0,tamano):
        indice = (llave_num+i)%tamano
        if map[indice] is None:
            map[indice] = ParllaveValor
            return indice
        else:
            i+=1
    return -1

def buscar(llave,map,tamano):
    print("\n\n- - - - - - - - - - - - - - - - - - - - -")
    print("Buscando a", llave)
    llave_num=(obtenerLlaveNumerica(llave))
    indice = llave_num%tamano
    ParKept=map[indice]
    if ParKept[0] == llave:
        print(map[indice])
        return indice
    else:
        return print("No encontrado")



map=formaArreglo(10)#Creando tabla Hash

#10 es el tamaño que tiene la Tabla Hash
agregar("Hola9", "12213299", map,10)#GUARDADO
agregar("Hola4",12213214,map,10)#GUARDADO
agregar("Hola1",1221321,map,10)#GUARDADO
agregar("Hola2",1221322,map,10)#GUARDADO
agregar("Hola3",1221323,map,10)#GUARDADO
agregar("Hola5",1221325,map,10)#GUARDADO
agregar("Hola6",1221326,map,10)#GUARDADO
agregar("Hola7",1221327,map,10)#GUARDADO
agregar("Hola8",1221328,map,10)#GUARDADO
agregar("Hola10",1221310,map,10)#GUARDADO

print(map)#Imprimiendo la tabla Hash con los datos almacenados

print("\nPOSICION DE Hola1: ",buscar("Hola1",map,10))#Buscando la llave de 1 "Hola1", implementando la funcion buscar (en la tabla Hash)
print("\nPOSICION DE Hola2: ",buscar("Hola2",map,10))
print("\nPOSICION DE Hola4: ",buscar("Hola4",map,10))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("\nLLAVE DE Hola: ",buscar("Hola",map,10))

