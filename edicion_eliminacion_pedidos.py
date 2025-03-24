import json 
def  Guardar_cambios(mostrar_pedidos, productos_edicion):
    with open("encargos.json", "w") as actualizar_pedidos:
        json.dump(mostrar_pedidos, actualizar_pedidos, indent=4)
    with open("almacen.json", "w") as actualizar_stock:
        json.dump(productos_edicion, actualizar_stock, indent=4)
def editar_productos():
    from Menu_pedidos import menu_pedidos
    with open("encargos.json", "r") as mostrar:
        mostrar_pedidos = json.load(mostrar)
    print("PEDIDOS YA ENLISTADOS")
    for pedido, detalles in mostrar_pedidos.items():
        print(f"Pedido {pedido}: Cliente {detalles['Codigo del cliente']}")
    codigo_pedido_editar=input("ingrese el codigo del pedido a editar: ").strip()
    if codigo_pedido_editar not in mostrar_pedidos:
        print("El producto ingresado no existe o no ha sido ingresado")
        return
    print("Elija que opcion desea realizar")
    while True:
        try:
            while True:
                print("""
                    1. Editar informacion del pedido
                    2. Eliminar un pedido
                    3. Retroceder
                       """)
                print("Ingrese una opcion")
                decision=int(input("Opcion:"))
                if decision>4:
                    print("No existe esa opcion (opcion no valida)")
                if decision==1:
                    print("Editar informacion")
                    pedido=mostrar_pedidos[codigo_pedido_editar]
                    with open("almacen.json", "r") as cargar_productos_edicion:
                        productos_edicion=json.load(cargar_productos_edicion)
                    while True:
                        print("""
                    1. Agregar un producto
                    2. Cambiar cantidad de los productos
                    3. Eliminar un producto del pedido
                    4. Salir 
                    """)
                        decision_editar=int(input("ingrese la opcion a realizar:"))
                        if decision_editar==1:
                            print("Agregar un producto")
                            codigo_producto_agregar=input("Ingrese el codigo del producto").strip()
                            if codigo_producto_agregar not in productos_edicion:
                                print("Este producto no existe en el almacen o aun no se registra")
                                continue
                            print("Ingrese los nuevos datos")
                            comparar_cantidad=productos_edicion[codigo_producto_agregar]["cantidad"]
                            cantidad_editar=int(input("Ingrese la cantidad: "))
                            if cantidad_editar>comparar_cantidad:
                                print("se supera la cantidad que se quiere editar del producto en el pedido")
                                continue
                            precio_venta_nuevo=input("Ingrese el precio de venta")
                            linea_pedido_nuevo=int(input("ingrese la linea del pedido"))
                            nuevo_producto_editado={
                                "codigo del pedido": codigo_pedido_editar,
                                "codigo del producto": codigo_producto_agregar,
                                "cantidad": cantidad_editar,
                                "precio de venta": precio_venta_nuevo,
                                "linea del pedido": linea_pedido_nuevo
                            }
                            pedido["Productos"].append(nuevo_producto_editado)
                            productos_edicion[codigo_producto_agregar]["cantidad"] -= cantidad_editar
                            Guardar_cambios(mostrar_pedidos, productos_edicion)
                            print("Producto agregado exitosamente")
                        elif decision_editar==2:
                            print("Cambiar cantidad de los productos")
                            codigo_cambiar=input("Ingrese el codigo del producto que quiere modificar: ").strip()
                            for producto in pedido["Productos"]:
                                if producto["codigo del producto"]== codigo_cambiar:
                                    cantidad1=producto["cantidad"]
                                    cantidad2=int(input("Ingrese la nueva cantidad: "))
                                    diferencia = cantidad1-cantidad2
                                    productos_edicion[codigo_cambiar]["cantidad"] -= diferencia
                                    producto["cantidad"] = cantidad2
                                    Guardar_cambios(mostrar_pedidos, productos_edicion)
                                    print("Exito")
                        elif decision_editar==3:
                            print("Eliminar un pedido")
                            codigo_cambiar=input("Ingrese el codigo del producto que quiere modificar").strip()
                            for producto in pedido["Productos"]:
                                if producto["codigo del producto"]== codigo_cambiar:
                                    productos_edicion[codigo_cambiar]["cantidad"] += producto["cantidad"]
                                    pedido["Productos"].remove(producto)
                                    Guardar_cambios(mostrar_pedidos, productos_edicion)
                                    print("Producto eliminado del pedido.")
                                    break
                        elif decision_editar==4:
                            break
                elif decision==2:
                    print("Eliminar un pedido")
                    
        except ValueError:
            print("Error, ingreso de valor no valido en el programa, Devuelto al menu")

editar_productos()


    