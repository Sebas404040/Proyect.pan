def registro_productos():
    from Intermediarios import codigos
    print ("Ingrese los siguientes datos: ")
    codigo_pan=input("Ingrese el codigo del producto: ")
    producto=codigos.get(codigo_pan, False)
    if producto==True:
        print("producto ya existente")
        if producto==False:
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
        print (codigos)
    else:
        print("El producto con el codigo ingresado ya se encuentra registrado")
    
registro_productos()