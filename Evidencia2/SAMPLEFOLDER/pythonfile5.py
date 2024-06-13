# archivo_dummy.py

def saludar(nombre):
    """Función para saludar a una persona por su nombre."""
    mensaje = f"Hola, {nombre}!"
    return mensaje

def suma(a, b):
    """Función para sumar dos números."""
    return a + b

def factorial(n):
    """Función para calcular el factorial de un número."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def imprimir_lista(lista):
    """Función para imprimir los elementos de una lista."""
    for elemento in lista:
        print(elemento)

def main():
    print(saludar("Mundo"))
    
    resultado_suma = suma(5, 7)
    print(f"La suma de 5 y 7 es: {resultado_suma}")
    
    numero = 5
    resultado_factorial = factorial(numero)
    print(f"El factorial de {numero} es: {resultado_factorial}")
    
    lista = [1, 2, 3, 4, 5]
    print("Elementos de la lista:")
    imprimir_lista(lista)

if __name__ == "__main__":
    main()
