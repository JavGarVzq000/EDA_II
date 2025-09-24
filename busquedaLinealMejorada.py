#Busqueda Lineal Mejorada
def busquedaLinealMejorada(A,n,x):
    encontrado=-1
    for k in range (n):
        if A[k] == x:
            encontrado=k
            break
    return encontrado

A=[1,4,6,8,9,11]
print(busquedaLinealMejorada(A,5,8))