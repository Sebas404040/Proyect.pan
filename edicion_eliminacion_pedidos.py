import json 
def editar_productos():
    from Menu_pedidos import menu_pedidos
    with open("encargos.json", "r") as mostrar:
        mostrar_pedidos = json.load(mostrar)
    print("PEDIDOS YA ENLISTADOS")
    for pedido, detalles in mostrar_pedidos.items():
        print(f"Pedido {pedido}: Cliente {detalles['Codigo del cliente']}")
    codigo_pedido_editar=input("ingrese el codigo del pedido a editar: ").strip()
    verificacion_edicion=mostrar_pedidos.get(codigo_pedido_editar, False)
    if verificacion_edicion==True:
        print("Elija que opcion desea realizar")
        while True:
            try:
                while True:
                    print("""
                        1. Editar informacion del pedido
                        2. Eliminar un pedido
                        3. Eliminar un producto
                        4. Retroceder
                           """)
                    print("Ingrese una opcion")
                    decision=int(input("Opcion:"))
                    if decision>4:
                        print("No existe esa opcion (opcion no valida)")
                    if decision==1:
                            print("Editar informacion")
                            pedido=pedidos[codigo_pedido]
                            with open("almacen.json", "r") as cargar_productos_edicion:
                                productos_edicion=json.load(cargar_productos_edicion)
                            while True:
                                print("""
                            1. Agregar un producto
                            2. Cambiar cantidad de los productos
                            3. Eliminar un producto del pedido
                            4. Salir 
                        
                            """)
                    elif decision==2:
                        print("Eliminar un pedido")
            except ValueError:
                print("Error, ingreso de valor no valido en el programa, Devuelto al menu")
    else:
        print("codigo de pedido no existente")
        menu_pedidos()

editar_productos()


    