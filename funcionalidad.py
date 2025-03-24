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
    codigo_pedido=input("Ingrese el codigo del pedido: ")
    with open("encargos.json", "r") as verificador_pedidos:
        verificacion_pedidos=json.load(verificador_pedidos)
    verificacion_pedidos=referencias.get(codigo_pedido, False)
    if verificacion_pedidos==False:
        codigo_cliente=input("ingrese el codigo del cliente: ")
        fecha_pedido=input("ingrese la fecha del pedido: ")
        print("A continuacion, ingrese los detalles del pedido")
        pedido= {
            "Codigo del cliente": codigo_cliente,
            "Fecha del pedido": fecha_pedido
            }
        
        numero_productos=int(input("Cuantos productos desea ingresar: "))
        with open ("almacen.json", "r") as obtener_precio:
            productos=json.load(obtener_precio)

        for cuenta in range(numero_productos):

            print("ingrese los productos para ingresarlos al pedido")
            ingresar_producto=input("Codigo del producto: ").strip()
            stock=int(input("Ingrese la cantidad a pedir: "))
            codigo_producto=productos.get(ingresar_producto, {})
            linea_pedido=int(input("Ingrese la linea del pedido: "))
            if not codigo_producto:
                print("codigo no existe")
            precio_venta = codigo_producto.get("precio venta",0)
            conjunto_pedido={
                "codigo del pedido": codigo_pedido,
                "codigo del producto":ingresar_producto,
                "cantidad": stock,
                "Precio cada unidad":precio_venta,
                "linea del pedido":linea_pedido
            }
            conjunto_pedidos[codigo_pedido]=conjunto_pedido
            pedido.update(conjunto_pedidos)
            referencias[codigo_pedido]=pedido

            with open("encargos.json", "w") as agregar:
                json.dump(referencias, agregar)
            
            obtener_cantidad=productos.get(ingresar_producto)
    else:
        print("Pedido ya ingresado")