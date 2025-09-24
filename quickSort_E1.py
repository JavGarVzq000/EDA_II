def intercambia(A,x,y):#Definicion de la funcion intercambia,
                       #cuyos parametros son: - el arreglo unidimensional
                       #                      - indice del elemento a cambiar de posicion
                       #                      - indice del otro elemento con el que se realizara el cambio
    tmp = A[x]#asignacion del valor ubicado en el primer indice del arreglo a cambiar, a la variable temporal
    A[x] = A[y]#asignacion del valor ubicado en el indice al que se le cambiara el 
    A[y] = tmp#asignacion del valor almacenado en tmp para el indice cuyo espacio se encuentra vacio

def particionar(A,p,r):#Definicion de la funcion particionar
                       #cuyos parametros son:
                       #                      - el arreglo unidimensional
                       #                      - el indice inferior del arreglo
                       #                      - indice superior (la longitud del arreglo - 1)
    print(A)#impresion del arreglo
    x=A[p]#asignacion del valor del primer elemento del arreglo a la variable x
    print(x)#impresion de dicho valor almacenado en x
    i=p#asignacion del indice inferior (primer indice) a la variable i
    for j in range(p+1,r+1):#Estructura for en que j va del valor siguiente del indice inferior, al indice superior
                            #(cabe hacer incapie que esta estructura se queda en el valor antecesor del limite superior
                            # es por eso que se le agrega una unidad en este caso)
        if (A[j]<=x):#Estructura de comparacion. se compara el valor almacenado en el arreglo posicion j con el valor almancenado en x
            i=i+1 #incremento en el valor de i, para ejecutar de nuevo la estructura
            intercambia(A,i,j)#llamado a la funcion intercambia con los valores cambiados
    intercambia(A,i,p)#Llamado a la funcion intercambia para no realizar cambios 
    return i #retornar el valor de i


def Quicksort(A,p,r):#Funcion Quicksort
                     #cuyos parametros son:
                     #                     - el arreglo unidimensional
                     #                     - el indice inferior del arreglo
                     #                     - indice superior (la longitud del arreglo - 1)
    if(p<r):#Estructura que evalua si el arreglo es mayor de una unidad
        q=particionar(A,p,r)#asignando el valor que retorna la variable i de particionar
        Quicksort(A,p,q-1)#Recursividad, trabajando la primera mitad del arreglo
        Quicksort(A,q+1,r)#Recursividad, trabajando la segunda mitad del arreglo


A=[5,4,3,2,1,0]#Arreglo propuesto
Quicksort(A,0,len(A)-1)#Llamado a la funcion Quicksort para ordenar el arreglo
                       #Se le entrega el arreglo, el primer indice (cero), y la longitud de dicho arreglo menos uno
print("Arreglo ordenado")#Imprimiendo "Arreglo ordenado"
print(A)#Imprimiendo el arreglo ordenado