def menu_pedidos():
    from Inicio import inicio_principal 
    while True:
        try:
            while True:
                print("""
                      1. Registro de productos
                    2. Almacenamiento de productos
                    3. Retroceder
                    """)
                print("Ingrese una opcion")
                decision=int(input("Opcion:"))
                if decision>2:
                    print("No existe esa opcion (opcion no valida)")
                if decision==1:
                    print("Registro de productos")
                elif decision==2:
                    print("Almacenamiento de productos")
                elif decision==3:
                    print("Retrocediendo...")
                    inicio_principal()
        except ValueError:
            print("Error, ingreso de valor no valido en el programa, Devuelto al menu")
                
                
menu_pedidos()
