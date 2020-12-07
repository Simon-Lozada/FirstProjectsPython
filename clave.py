print("ponga la contraseña clave") #aqui le digo a mi usuario que ponga la contraseñ correta 
caracteres = [1,2,3] # defino la cadena de caracteres
clave = "pvkultsra" # defino la clave 
for i in caracteres: # hago un ciclo for 
    usuario = str(input("diga la clave: ")) #le pido al usuario la clave 
    if usuario == clave: # si el usuario pene la clave correta se lo informo 
      print("clave correcta ") 
    elif i == 3 : # en caso contrario lo informo que la clave es in correcta 
        print("clave incorrecta")