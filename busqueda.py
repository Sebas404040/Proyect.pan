import json
def buscar_productos_pedidos():
    from Inicio import inicio_principal
    print("""
        1. Buscar Productos
        2. Buscar pedidos
        3. Regresar
       """)
    print("Ingrese una opcion")
    decision_busqueda=int(input("Opcion: "))
    if decision_busqueda>3:
        print("Opcion no valida")
    if decision_busqueda==1:
        print("Buscar productos")
        codigo_busqueda=input("Ingrese el codigo del producto: ").strip()
        with open ("almacen.json", "r") as buscador:
            memoria_productos=json.load(buscador)
        producto= memoria_productos.get(codigo_busqueda)
        if producto:
            print("BUSQUEDA TERMINADA")
            print("Codigo del producto", codigo_busqueda)
            print("    Nombre del producto", producto["nombre"])
            print("    Cantidad Disponible:", producto['cantidad'])
            print("    Precio:", producto['precio_venta'])
            print("--------------------------------------------------")
        else: 
            print("Producto no encontrado")
        inicio_principal()
    elif decision_busqueda==2:
        print("Buscar pedidos")
    elif decision_busqueda==3:
        print("Regresar")

    