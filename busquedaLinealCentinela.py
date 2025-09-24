#Busqueda Lineal Centinela
def busquedaLinealCentinela(A,n,x):
    tmp = A[n]
    A[n] = x
    k = 0
    while A[k] != x:
        k=k+1
    A[n]=tmp
    if k<n or A[n]==x:
        return k
    else: 
        return -1
    #return encontrado
A=[1,4,6,8,9,10]
print(busquedaLinealCentinela(A,5,10))
