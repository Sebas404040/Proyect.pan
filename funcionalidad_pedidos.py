def registro_pedidos():
    import json
    from Intermediarios import referencias
    print ("Ingrese los siguientes datos: ")
    codigo_pedido=input("Ingrese el codigo del pedido: ")

    with open("almacen.json", "r") as verificador_pedidos:
        verificacion_pedidos=json.load(verificador_pedidos)
    verificacion_pedidos=referencias.get(codigo_pan, False)

    if verificacion_pedidos==False:
        codigo_cliente=input("ingrese el codigo del cleinte: ")
        fecha_pedido=input("ingrese la fecha del pedido: ")
        Detalles_pedido=input("ingrese los detalles del pedido: ")
        cantidad_stock=input("ingrese la cantidad disponible del producto: ")
        precio_venta=input("ingrese el precio al dirigido al cliente: ")
        precio_proveedor=input("ingrese el precio del proveedor: ")
        pedido= {
            "Codigo del pedido": codigo_pedido,
            "Codigo del cliente": codigo_cliente,
            "Fecha del pedido": fecha_pedido,
            "Detalles del pedido": Detalles_pedido,
            "cantidad": cantidad_stock,
            "precio_venta": precio_venta,
            "precio_proveedor": precio_proveedor
        }
        referencias[codigo_pedido]= pedido

        with open("almacen.json", "w") as agregar:
            json.dump(referencias, agregar)
        print (referencias)
    else:
        print("El producto con el codigo ingresado ya se encuentra registrado")