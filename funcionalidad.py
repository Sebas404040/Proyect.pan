import json 
def registro_productos():
    print("Ingrese los siguientes datos: ")
    codigo_pan = input("Ingrese el código del producto: ")

    try:
        with open("almacen.json", "r") as archivo:
            productos = json.load(archivo)  
    except (FileNotFoundError, json.JSONDecodeError):
        productos = {} 
    
    if codigo_pan in productos:
        print("ERROR, Producto ya existente")
        return
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría: ")
    descripcion = input("Ingrese alguna característica: ")
    proveedor = input("Ingrese proveedor: ")
    cantidad_stock = int(input("Ingrese la cantidad disponible del producto: "))
    precio_venta = int(input("Ingrese el precio dirigido al cliente: "))
    precio_proveedor = int(input("Ingrese el precio del proveedor: "))

    producto = {
        "nombre": nombre,
        "categoria": categoria,
        "descripcion": descripcion,
        "proveedor": proveedor,
        "cantidad": cantidad_stock,
        "precio_venta": precio_venta,
        "precio_proveedor": precio_proveedor
    }

  
    productos[codigo_pan] = producto


    with open("almacen.json", "w") as agregar:
        json.dump(productos, agregar, indent=4) 

    print("Se agrego el producto")  

    

def almacenar_productos():
    import json
    with open("almacen.json", "r") as mostrar:
        mostrar_productos = json.load(mostrar)

    print("PRODUCTOS ENLISTADOS")
    
    for codigo, detalles in mostrar_productos.items():
        print("Código:", codigo)
        for clave, valor in detalles.items():
            print(f"{clave}: {valor}")

def registro_pedidos():
    import json
    conjunto_pedidos={}
    from Intermediarios import referencias
    print ("Ingrese los siguientes datos: ")
    codigo_pedido = input("Ingrese el código del pedido: ").strip()
    with open("encargos.json", "r") as verificador_pedidos:
        verificacion_pedidos=json.load(verificador_pedidos)
    verificacion_pedidos=referencias.get(codigo_pedido, False)
    if verificacion_pedidos==False:
        codigo_cliente=input("ingrese el codigo del cliente: ")
        fecha_pedido=input("ingrese la fecha del pedido: ")
        print("A continuacion, ingrese los detalles del pedido")
        pedido= {
            "Codigo del cliente": codigo_cliente,
            "Fecha del pedido": fecha_pedido,
            "Productos": []
         }
        
        
        numero_productos=int(input("Cuantos productos desea ingresar: "))
        with open ("almacen.json", "r") as obtener_precio:
            productos=json.load(obtener_precio)

        for cuenta in range(numero_productos):

            print("ingrese los productos para ingresarlos al pedido")
            ingresar_producto=input("Codigo del producto: ").strip()
            if ingresar_producto not in productos:
                print("Este producto no existe, ingrese uno valido")
                continue
            stock=int(input("Ingrese la cantidad a pedir: "))
            codigo_producto=productos.get(ingresar_producto, {})
            linea_pedido=int(input("Ingrese la linea del pedido: "))
            if not codigo_producto:
                print("codigo no existe")
            precio_venta = productos[ingresar_producto].get("precio_venta",0)
            stock_disponible= productos[ingresar_producto].get("cantidad",0)
            if stock>stock_disponible:
                print("cantidades no disponibles para la cantidad pedida")
                continue
            productos[ingresar_producto]["cantidad"]-=stock
            conjunto_pedido={
                "codigo del pedido": codigo_pedido,
                "codigo del producto":ingresar_producto,
                "cantidad": stock,
                "Precio cada unidad":precio_venta,
                "linea del pedido":linea_pedido
            }
            pedido["Productos"].append(conjunto_pedido)
            with open ("almacen.json", "r") as contador:
                tomar_productos=json.load(contador)
            cantidad_producto=tomar_productos[ingresar_producto].get("cantidad", 0)
            print (cantidad_producto)
        referencias[codigo_pedido] = pedido
        
        with open("encargos.json", "w") as agregar_pedido:
            json.dump(referencias, agregar_pedido, indent=4)

        with open("almacen.json", "w") as actualizar_stock:
            json.dump(productos,actualizar_stock, indent=4)


    else:
        print("Codigo de pedido ya ingresado")