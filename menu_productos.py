def menu_productos():
    from funcionalidad import registro_productos, almacenar_productos
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
                decision_producto=int(input("Opcion:"))
                if decision_producto>3:
                    print("No existe esa opcion (opcion no valida)")
                if decision_producto==1:
                    print("Registro de productos")
                    registro_productos()
                elif decision_producto==2:
                    print("Almacenamiento de productos")
                    almacenar_productos()
                elif decision_producto==3:
                    print("Retrocediendo...")
                    decision_producto==0
                    inicio_principal()
                    
        except ValueError:
            print("Error, ingreso de valor no valido en el programa, Devuelto al menu")
                           