def menu_pedidos():
    from Inicio import inicio_principal 
    while True:
        try:
            while True:
                print("""
                    1. Creacion de pedidos
                    2. Registro de productos
                    3. Editar pedidos
                    """)
                print("Ingrese una opcion")
                decision=int(input("Opcion:"))
                if decision>4:
                    print("No existe esa opcion (opcion no valida)")
                if decision==1:
                    print("Creacion de productos")
                elif decision==2:
                    print("Registro de productos")
                elif decision==3:
                    print("Editar productos")
                elif decision==4:
                    print("Retrocediendo")
                    inicio_principal()
        except ValueError:
            print("Error, ingreso de valor no valido en el programa, Devuelto al menu")
                
                

