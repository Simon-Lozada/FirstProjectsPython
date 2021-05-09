print("choose the numbers for the operation")
num1 = float(input("choose a number: "))
num2 = float(input("choose a number: "))

print("now choose the operation you want to execute your options are:"f"\nM = Multiplication"f"\nS = sum"f"\nR = subtraction"f"\nD = Division")
operacion = input("Choose the operation: ")


if operacion == "S":
    sum = num1 + num2 
    print (f"\nThe sum es: {sum}")

if operacion == "R":
    subtraction = num1 - num2 
    print (f"\nThe subtraction es: {subtraction}")

if operacion == "M":
    Multiplication = num1 * num2 
    print (f"\nThe Multiplication es: {Multiplication}")

if operacion == "D":
    Division = num1 / num2 
    print (f"\nThe Division es: {Division}")


