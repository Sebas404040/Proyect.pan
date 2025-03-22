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
