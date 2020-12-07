print("Introdusca los valores para la lista")

# Los elementos de la lista

lista = [input("ponga el Primer Valor: "), input("ponga el Segundo Valor: "), input("ponga el Tercer Valor: "), input(" ponga el Cuarto Valor: "), input("ponga el Quinto Valor: ")]

print(f" \nComponentes de la lista: {lista[0]}, {lista[1]}, {lista[2]}, {lista[3]}, {lista[4]}")

accion = "y"

# Para que, en el caso de que el usuario no coloque una accion correcta, tenga la oportunidad de repetir 

while accion!="x":

    # Preguntandole si desea eliminar un elemento de la lista o si lo quiere dejar asi

    accion = input("\nQuiere hacer algun cambio en la lista ?: ")
    print("para añadir algun elemento  , 'añadir'")
    print("para eliminar algun elemto  ,'eliminar' ")
    print("Para hacer los dos ponga ,'ambos' ")

    # En el caso de que si

    while accion == "si":

        # Preguntandole si quiere eliminar y/o añadir un elemento

        seleccion = input("\n¿Quiere eliminar o añadir un elemento (Pueden elegirse ambas)?: ")
        
        # En el caso de que quiera añadir algun elemento 
        if seleccion == "añadir":
                insertar = input("\n¿Que elemento quiere insertar?: ")#pregunto que elemento quiere añadir 
                pocicion = int(input("\n¿En que pocicion?: "))#le pido la posicion que quiere que tome 
           
                lista.insert(pocicion-1,insertar)#y lo inserto 
                accion = "x"

                print("\nÂ¡Elemento agregado!")

        # En el caso de que quiera eliminar algun elemento de la listas
        
        if seleccion == "eliminar" :
                eliminar = input("\n¿Que elemento quiere eliminar?: ")

                lista.remove(eliminar)#(Me doy cuenta que si enves de decir el nombre del elemnto  a eliminar pones la posicion lo toma como un error)
                accion = "x"

                print("\n¡Elemento eliminado!")

        # En el caso de que quiera hacer ambas acciones

        if seleccion == "ambos":
                #aqui insertamos
                insertar = input("\n¿Que elemento quiere insertar?: ")
                accion = int(input("\n¿En que pocicion?: "))
                lista.insert(accion - 1, insertar)
                #aqui eliminamos 
                eliminar = input("\n¿Que elemento quiere eliminar?: ")#(Me doy cuenta que si enves de decir el nombre del elemnto  a eliminar pones la posicion lo toma como un error pero igual )
                
                lista.remove(eliminar)

                accion = "x"

        # En el caso de que la accion sea invalida

        elif accion!="x":
                print("\nEsa no es una accion , no es posible ")

    # En el caso que desde un principio haya dicho que no queria modificar la lista

    if accion == "no":
        print("\nOperacion terminada")

        accion = "x"

    # En el caso que haya puesto cualquier cosa invalida

    else:
        print("\nEsa no es una accion Valida, intente de nuevo")

print(lista)