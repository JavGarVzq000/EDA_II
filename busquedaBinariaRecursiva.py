#Busqueda Binaria Recursiva
import math
def BusquedaBinRecursiva(A,x,izquierda,derecha):
    if izquierda > derecha:
        return -1
    medio = math.floor((izquierda+derecha)/2)
    print(medio,"valor medio")

    if(A[medio]==x):
        return medio
    elif(A[medio]<x):
        return BusquedaBinRecursiva(A,x,medio+1,derecha)
    else:
        return BusquedaBinRecursiva(A,x,izquierda,medio-1)

A=[10,20,30,40,50,60,70,80]
x=10
izquierda=0
derecha=7
print(BusquedaBinRecursiva(A,x,izquierda,derecha))