print("Enter the values for the list")

# List items

list = [input("put the First Value: "), input("put the Second Value: "), input("put the Third Value: "), input("put the Fourth Value: "), input("put the Fifth Value: ")]

print(f" \nList components: {list[0]}, {list[1]}, {list[2]}, {list[3]}, {list[4]}")

action = "y"

# So that, in the event that the user does not place a correct action, they have the opportunity to repeat

while action!="x":

    # Asking if you want to remove an item from the list or if you want to leave it that way

    action = input("\nDo you want to make any changes to the list ?: ")
    print("to add an element, 'add'")
    print("to remove an element, 'remove'")
    print("To do both put, 'both'")

    # In the event that yes

    while action == "yes":

        # Asking if you want to remove and / or add an item

        selection = input("\nDo you want to remove or add an item (Both can be chosen) ?: ")
        
        # In case you want to add an element
        if selection == "add":
                insertar = input("\nWhat element do you want to insert ?: ")#Ask what element you want to add
                pocicion = int(input("\nIn what position?: "))# I ask you for the position you want me to take
           
                list.insert(pocicion-1,insertar)#and insert it
                action = "x"

                print("\nItem added!")

        # In case you want to remove an item from the lists
        
        if selection == "remove" :
                remove = input("\nWhat item do you want to delete ?: ")

                list.remove(remove)# (I realize that if you say the name of the element to delete, you put the position, it takes it as an error)
                action = "x"

                print("\n¡Elemento eliminado!")

        #In case you want to do both actions

        if selection == "ambos":
                # here we insert
                insertar = input("\n¿What element do you want to insert ?: ")
                action = int(input("\n¿En que pocicion?: "))
                list.insert(action - 1, insertar)
                #here we eliminate
                remove = input("\n¿What element do you want to remove ?: ")# (I realize that if you say the name of the element to delete, you put the position, it takes it as an error but still )
                
                list.remove(remove)

                action = "x"

       # In the event that the action is invalid

        elif action!="x":
                print("\nThat is not an action, it is not possible")

        # En el caso que desde un principio haya dicho que no queria modificar la lista

    if action == "no":
        print("\nOperation completed")

        action = "x"

# In case you have put anything invalid
    else:
        print("\nThis is not a valid action, try again")

print(list)
