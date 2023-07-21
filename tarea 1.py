def cuadrado(alto, ancho):
    for i in range(0, alto):
        for j in range(0, ancho):
            print("* ", end="")
        print()

def triangulo(lado):
    for i in range(lado):
        for j in range(lado-i-1):
            print(" ", end=" ")
        for k in range(2*i+1):
            print("*", end=" ")
        print()
    
def flecha(lado):
    for i in range(lado):
        print(' ' * (lado-i-1) + "*" * (2*i+1))
    for j in range(int(lado)):
        print(' ' * int(lado - lado/2) + '*' * int(lado-1))

if __name__ == "__main__":
    print('CUADRADO')
    cuadrado(5,5)
    print('\n')
    print('TRIANGULO')
    triangulo(5)
    print('\n')
    print('ARBOL')
    flecha(5)