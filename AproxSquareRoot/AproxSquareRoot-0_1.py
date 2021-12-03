x = int(input("Ingrese el numero al que quiere aproximar la raiz cuadrada (Debe ser entero): "))

elevado = 1
resultado = 0
elevado1= 0

for i in range(0,x):
    elevado += 1
    elevado1 = elevado * elevado
    if elevado1 <= x:
        resultado = elevado1
    elif elevado1> x:
        elevado -=1
        break

if x != resultado:
    solucion = (x-resultado)/(2*elevado)
    print(solucion + elevado)
elif x == resultado:
    print(elevado)