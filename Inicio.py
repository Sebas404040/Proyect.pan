
def inicio_principal():
    from menu_productos import menu_productos
    from Menu_pedidos import menu_pedidos
    from busqueda import buscar_productos_pedidos
    try:
        while True:
            print("""
                PANADERIA "Chavo, tengo hambre "titittititi""
                1. Productos
                2. Pedidos
                3. Busqueda de productos
                4. Cerrar programa
                """)
            print("Ingrese una opcion")
            decision=int(input("Opcion:"))
            if decision>4:
                print("No existe esa opcion (opcion no valida)")
            if decision==1:
                print("productos")
                menu_productos()
            elif decision==2:
                print("Pedidos")
                menu_pedidos()
            elif decision==3:
                print("Busqueda de productos")
                buscar_productos_pedidos()
            elif decision==4:
                print("Saliendo...")
                break
    except ValueError:
        print("Error, ingreso de valor no valido en el programa, intente reiniciar")
                

        
    