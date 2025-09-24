def formaArreglo(tamano):#Funcion para formar un arreglo, definiendo el tamaño desde el teclado, parametro: tamano
    Arr=[None]*tamano#creacion de un arreglo vacio del tamaño sugerido con la variable tamano
    return Arr#retornando el arreglo creado

def obtenerLlaveNumerica(llave):#Funcion para obtener una llave numerica de llave (el dato a almacenar)
    hash=0#Declarando variable hash en cero
    for char in str(llave):#estructura repetitiva que va a evaluar la llave caracter por caracter
        hash+=ord(char)#SI se tiene un caracter se va a realizar la sumatoria de los valores ASCII de llave. (ord obtiene el valor ASCII)
    return hash#Retorna la sumatoria hash

def H(llaveN):#Funcionpara determinar que posicion de almacenamiento tendra el dato llaveN
    return llaveN%5#Obteniendo su posicion aplicando dato modulo entre 5, el resto de la division entera que nos regrese sera la posicion

def agregar(llave,valor,map,tamano):#Funcion para agregar un dato con sus respectivos datos necesarios para identificarlo de varias maneras.
                                    #Parametros: llave, valor, map (tabla Hash), tamano
    llave_hash=H(obtenerLlaveNumerica(llave))#En la variable llave_hash se hace un llamado a obtenerLlaveNumerica para llave y luego darle una posicion con H
    ParllaveValor=[llave,valor]#En la variable ParllaveValor se va a almacenar la llave y su valor correpondiente
    if map[llave_hash] is None:#Estructura condicional que evalua si la tabla Hash tiene un valor almacenado en una determinada posicion o no.
        map[llave_hash]=list([ParllaveValor])#En caso de estar vacia la posicion se va a almacenar la informacion par (llave y su valor), en ParllaveValor
                                            #y la funcion de Python list los almacenara en la posicion dada de llave_hash en el mapa
        return True#Retornando verdadero, que ya se ocupo el lugar
    else:#En otro caso (SOLUCIONANDO COLISIONES CON HASHING ABIERTO)
        for par in map[llave_hash]:#Estructura de repeticion que opera dentro de la Tabla Hash
            if par[0]==llave:#Estructura condicional que evalua si el valor a insertar sea igual al que ya se encuentra insertado
                par[1]=valor#Se almacena el valor del par en la variable en turno dentro de la tabla Hash
                return True#Retorna que ya esta ocupado por un dato almacenado

        for j in range(tamano):#estructura de repeticion que opera dentro del tamaño fijado anteriormente con tamano
            llaveh=(llave_hash+j)%13#HASHING ABIERTO: aqui se encuentra solucion para fijar un nuevo destino para almacenar un dato en la Tabla Hash
            if(llaveh==len(map)):#estructura condicional que nos ayuda a no sobrepasar los limites de la tabla Hash
                print("Tabla llena", llave_hash)#imprimiendo "Tabla llena" en caso de que se llegue al limite fijado con la estructura
                break#Rompe el ciclo
            else:#En otro caso, estar dentro del limite de la tabla Hash
                if map[llaveh]is None:#Estructura condicionalq ue evalua si la posicion determinada por llaveh en la Tabla Hash esta vacia
                    map[llaveh]=list([ParllaveValor])#En caso de estar vacia la posicion se va a almacenar la informacion par (llave y su valor), en ParllaveValor
                                                    #y la funcion de Python list los almacenara en la posicion dada de llave_hash en el mapa
                    return True#Retornar True, ya esta ocupado

def buscar(llave,tamano):#Funcion buscar que recibe las dos claves del dato que se espera almacenado
    llave_hash=H(obtenerLlaveNumerica(llave))#se obtiene la llave_hash para buscar el dato en la tabla Hash

    if map[llave_hash] is not None:#Estructura condicional que evalua si la posicion llave_hash no esta vacia 
        for par in map[llave_hash]:#Estructura de repeticion que recorre la Tabla Hash, en la posicion dictada por llave_hash
            if par[0]==llave:#Estructura condicional que revisa si el la informacion 1 (llave) almacenado es igual al del dato buscado
                return par[1]#En caso de ser igual, se retorna el valor del dato almancedao. ESE ES EL PAR 

            else:#En otro caso...
                for j in range(tamano):#Estructura de repeticion que recorre con j en razon de tamano
                    llaveh=(llave_hash+j)%13#se obtiene la llaveh con el modulo de la llave_hash y el valor de j en turno %13
                    if (llaveh==len(map)):#Estructura condicional que evalua si estamos dentro de los limites de la tabla Hash
                        break#Se rompe el curso de esta estructura, no se hace algo mas
                    for par1 in map[llaveh]:#estructura de repeticion que recorre dentro de los limites de la tabla Hash
                        if par1[0]==llave:#Estructura condicional que evalua la llave almacenada en el par1, con el del dato buscado
                            return par1[1]#En caso de ser correcto, igual, se retorna el valor del par.
    return None#No se retorna algun dato puntual

map=formaArreglo(10)#Creando tabla Hash

#10 es el tamaño que tiene la Tabla Hash
agregar("Hola6",1221326,map,10)
agregar("Hola7",1221327,map,10)
agregar("Hola8",1221328,map,10)
agregar("Hola10",1221310,map,10)


print(map)#Imprimiendo la tabla Hash con los datos almacenados

print("\nLLAVE DE 1: ",buscar("Hola11",10))#Buscando la llave de 1 "Hola1", implementando la funcion buscar (en la tabla Hash)

print("\nLLAVE DE 1: ",buscar("Hola10",10))#Buscando la llave de 1 "Hola1", implementando la funcion buscar (en la tabla Hash)

