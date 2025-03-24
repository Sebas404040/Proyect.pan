def menu_pedidos():
    from edicion_eliminacion_pedidos import editar_productos
    from funcionalidad import registro_pedidos
    from Inicio import inicio_principal 
    while True:
        try:
            while True:
                print("""
                    1. Creacion de pedidos
                    2. Editar pedidos
                    3. Retroceder
                    """)
                print("Ingrese una opcion")
                decision=int(input("Opcion:"))
                if decision>4:
                    print("No existe esa opcion (opcion no valida)")
                if decision==1:
                    print("Creacion de pedidos")
                    registro_pedidos() 
                elif decision==2:
                    print("Editar pedidos")
                    editar_productos()
                elif decision==3:
                    inicio_principal()
        except ValueError:
            print("Error, ingreso de valor no valido en el programa, Devuelto al menu")
                
                

