print("elija los numeros para la opercion")
num1 = float(input("elija un numero: "))
num2 = float(input("elija un numero: "))

print("ahora elija la operacion  que desea ejecuatar sus opciones son:"f"\nM = Multiplicacion"f"\nS = suma"f"\nR = Resta"f"\nD = Division")
operacion = input("elija una operacon: ")


if operacion == "S":
    suma = num1 + num2 
    print (f"\nLa suma es: {suma}")

if operacion == "R":
    resta = num1 - num2 
    print (f"\nLa resta es: {resta}")

if operacion == "M":
    Multiplicacion = num1 * num2 
    print (f"\nLa resta es: {Multiplicacion}")

if operacion == "D":
    division = num1 / num2 
    print (f"\nLa Divison es: {division}")


