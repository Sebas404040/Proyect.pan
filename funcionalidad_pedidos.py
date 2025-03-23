def registro_pedidos():
    import json
    from Intermediarios import referencias
    print ("Ingrese los siguientes datos: ")
    codigo_pedido=input("Ingrese el codigo del pedido: ")

    with open("encargos.json", "r") as verificador_pedidos:
        verificacion_pedidos=json.load(verificador_pedidos)
    verificacion_pedidos=referencias.get(codigo_pedido, False)

    if verificacion_pedidos==False:
        numero_verificar=int(input("Ingrese cuantos productos va a pedir: "))
        with open("almacen.json", "r") as verificacion_existencias:
            verificar_existencias=json.load(verificacion_existencias)
        numero_productos= verificar_existencias.values()
        for i in verificar_existencias.values():
            numero_productos+=len(i)

        if numero_productos<=numero_verificar:
            codigo_cliente=input("ingrese el codigo del cleinte: ")
            fecha_pedido=input("ingrese la fecha del pedido: ")
            pedido= {
                "Codigo del pedido": codigo_pedido,
                "Codigo del cliente": codigo_cliente,
                "Fecha del pedido": fecha_pedido,
                "Detalles del pedido": Detalles_pedido
                }
            referencias[codigo_pedido]=pedido

            with open("almacen.json", "w") as agregar:
                json.dump(referencias, agregar)
            print (referencias)

            print("A continuacion, ingrese los detalles del pedido")
            Detalles_pedido=input("ingrese los detalles del pedido: ")
        else:
            print("El valor ingresado supera los productos ya almacenados")

    else:
        print("El producto con el codigo ingresado ya se encuentra registrado")

            
          