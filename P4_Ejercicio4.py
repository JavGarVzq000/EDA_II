def busquedaLinealRecursiva(A, x, izquierda, derecha):
    if izquierda > derecha:
        encontrado = -1
    else:
        if A[izquierda] == x:
            encontrado = izquierda
        else:
            encontrado = busquedaLinealRecursiva(A, x, izquierda + 1, derecha)
    return encontrado

A = [10, 20, 30, 40, 50, 60, 70, 80, 90]
x = 50
izquierda = 0
derecha = len(A) - 1
print(busquedaLinealRecursiva(A, x, izquierda, derecha))