def menu_pedidos():
    from Inicio import inicio_principal 
    while True:
        try:
            while True:
                print("""
                    1. Creacion de pedidos
                    2. Registro de productos
                    3. Editar pedidos
                    4. Eliminar pedidos
                    5. Retroceder
                    """)
                print("Ingrese una opcion")
                decision=int(input("Opcion:"))
                if decision>4:
                    print("No existe esa opcion (opcion no valida)")
                if decision==1:
                    print("Creacion de pedidos")
                elif decision==2:
                    print("Registro de pedidos")
                elif decision==3:
                    print("Editar pedidos")
                elif decision==4:
                    print("Eliminar pedidos")
                elif decision==5:
                    inicio_principal()
        except ValueError:
            print("Error, ingreso de valor no valido en el programa, Devuelto al menu")
                
                

