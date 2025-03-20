
def inicio_principal():
    from menu_productos import menu_productos
    from Menu_inventario import menu_inventario
    from Menu_pedidos import menu_pedidos
    try:
        while True:
            print("""
                PANADERIA UFF QUE BIZCOCHO
                1. Productos
                2. Pedidos
                3. Almacenamiento de mercancia
                4. Busqueda de productos
                5. Cerrar programa
                """)
            print("Ingrese una opcion")
            decision=int(input("Opcion:"))
            if decision>5:
                print("No existe esa opcion (opcion no valida)")
            if decision==1:
                print("productos")
                menu_productos()
            elif decision==2:
                print("Pedidos")
                menu_pedidos()
            elif decision==3:
                print("Almacenamiento de mercancia")
                menu_inventario()
            elif decision==4:
                print("Busqueda de productos")
                
            elif decision==5:
                print("Saliendo...")
                break
    except ValueError:
        print("Error, ingreso de valor no valido en el programa, intente reiniciar")
                
inicio_principal()
        
    