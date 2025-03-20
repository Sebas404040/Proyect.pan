def menu_inventario():
    from Inicio import inicio_principal 
    while True:
        try:
            while True:
                print("""
                    1. Editar productos de inventario
                    2. Retroceder 
                    """)
                print("Ingrese una opcion")
                decision=int(input("Opcion:"))
                if decision>2:
                    print("No existe esa opcion (opcion no valida)")
                if decision==1:
                    print("Editar productos")
                elif decision==2:
                    print("Retrocediendo...")
                    inicio_principal()
        except ValueError:
            print("Error, ingreso de valor no valido en el programa, Devuelto al menu")
                
                

