def registro_productos():
    import json
    from Intermediarios import codigos
    print ("Ingrese los siguientes datos: ")
    codigo_pan=input("Ingrese el codigo del producto: ")

    with open("almacen.json", "r") as verificador:
        verificacion=json.load(verificador)
    verificacion=codigos.get(codigo_pan, False)

    if verificacion==False:
        nombre=input("ingrese el nombre del producto: ")
        categoria=input("ingrese la categoria: ")
        descripcion=input("ingrese alguna caracteristica: ")
        proveedor=input("ingrese proveedor: ")
        cantidad_stock=input("ingrese la cantidad disponible del producto: ")
        precio_venta=input("ingrese el precio al dirigido al cliente: ")
        precio_proveedor=input("ingrese el precio del proveedor: ")
        producto= {
            "nombre": nombre,
            "categoria": categoria,
            "descripcion": descripcion,
            "proveedor": proveedor,
            "cantidad": cantidad_stock,
            "precio_venta": precio_venta,
            "precio_proveedor": precio_proveedor
        }
        codigos[codigo_pan]= producto

        with open("almacen.json", "w") as agregar:
            json.dump(codigos, agregar)
        print (codigos)
    else:
        print("El producto con el codigo ingresado ya se encuentra registrado")
    

def almacenar_productos():
    import json
    with open("almacen.json", "r") as mostrar:
        mostrar_productos = json.load(mostrar)

    print("PRODUCTOS ENLISTADOS")
    
    for codigo, detalles in mostrar_productos.items():
        print("Código:", codigo)
        for clave, valor in detalles.items():
            print(f"{clave}: {valor}")