import math
def circulo(radio):
    A= round((math.pi*(radio*radio)), 3)
    return A

def triangulo(base, altura):
    A= round(((base*altura)/2), 3)
    return A

def cuadrado(ancho, alto):
    A= round((ancho*alto), 3)
    return A

def poligono(lados, medidaL):
    Ap= lados/2*math.tan(360/2*lados)
    P= lados*medidaL
    A= round(((P*Ap)/2), 3)
    return A

print('BIENVENIDO')
print('Este programa te permite encontrar el area de circulos, triangulos, rectangulos o cualquier poligono regular')
menu = """
Selecciona una opcion segun el area que quieras calcular
1. CIRCULO
2. POLIGONO
3. SALIR DEL PROGRAMA
"""
repetir = True
while repetir== True:
    print(menu)
    try:
        op = int(input('Ingresa opcion: '))
        if op is 1:
            r= float(input('Ingresa el radio: '))
            print('AREA = ' + str(circulo(r)))
        elif op is 2:
            l= int(input('¿Cuantos lados?: '))
            while l<3:
                print('No es un poligono')
                l= int(input('¿Cuantos lados?: '))
            if l==3:
                print('TRIANGULO')
                bt= float(input('Ingresa base: '))
                ht= float(input('Ingresa altura: '))
                print('AREA = ' + str(triangulo(bt,ht)))
            elif l==4:
                print('CUADRADO/RECTANGULO')
                bc= float(input('Ingresa base: '))
                hc= float(input('Ingresa altura: '))
                print('AREA = ' + str(cuadrado(bc,hc)))
            elif l>4:
                print('POLIGONO REGULAR')
                m= float(input('Ingresa la medida de los lados: '))
                print('AREA = ' + str(poligono(l,m)))
        elif op is 3:
            repetir= False
        else:
            print('ERROR. INGRESA UNA OPCION VALIDA')
    except:
        print('ERROR')