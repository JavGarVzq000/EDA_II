import random

A=[]
def creandoArray(k):
    if k>10 and k<30:
        for i in range(0,k):
            iniciar=random.randint(0,k)
            A.append(iniciar)

def newArrayLong(A):
    array = CreaLista(len(A))
    for i in range(0,len(A)):
        array[i+1] = A[i]
    return array

def oldArrayLong(A):
    array = CreaLista(len(A)-2)
    for i in range(1,len(A)):
        array[i-1] = A[i]
    return array

#Counting sort (Codigo Original)
def CreaLista(k):
    L=[]
    for i in range(k+1):
        L.append(0)
    return L

#Algoritmo de ordenamiento
def countingSort(A,k):#A es la lista y k es el valor maximo de la lista
    C=CreaLista(k)
    B=CreaLista(len(A)-1)
    for j in range(1,len(A)):
        C[A[j]]=C[A[j]]+1
    for i in range(1,k+1):
        C[i]=C[i]+C[i-1]
    for j in range(len(A)-1, 0,-1):
        B[C[A[j]]]=A[j]
        C[A[j]]=C[A[j]]-1
    return B #Retorna la lista de apoyo B, la ordenada

#Funcion main que une todos los puntos anteriores, funciones y movimientos principales del programa.
def main():
    print("\n\t- - - COUNTING SORT - - -\n")
    k = int(input("(k solo puede valer 10<k<30)\nIngrese el valor de k para el arreglo A: "))
    creandoArray(k)
    if A == []:
        print("\nNo se pudo generar el arreglo no cumple con las normas de k")
    else:
        print("Lista Original: ", A)
        newArreglo = newArrayLong(A)
        #Se implemento la funcion max que por defecto ofrece Python para determinar el elemento
        #mayor de un arreglo
        print("Lista Ordenada: ",oldArrayLong(countingSort(newArreglo,max(newArreglo))))

main()