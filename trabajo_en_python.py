"""
INGRESO de datos de productos
El sistema debe permitir ingresar datos básicos de los productos: 
nombre, categoría, y precio (sin centavos). 
Estos datos deben almacenarse en una lista, donde cada cliente sea representado/a como 
una sublista de tres elementos (nombre, categoría, y precio).

VISUALIZACIÓN de productos registrados
El programa debe incluir una funcionalidad para mostrar en pantalla todos los productos 
ingresados. 
La información debe presentarse de manera ordenada y legible, con cada producto numerado.

"""
opcion = 0
productos=[]

#MENU
while opcion != 5:
    print("\n=== GESTION DE PRODUCTOS ===\n1. Agregar producto\n2. Mostrar productos" \
    "\n3. Buscar producto\n4. Eliminar producto\n5. Salir del programa")

    opcion = int(input("\nSeleccione una opción: "))

    if opcion == 5:
        print("saliendo del programa")
        break

    #VERIFICAMOS QUE LA OPCION ESTE DENTRO DEL PARAMETRO
    if opcion<1 or opcion>5:
        print("\nDebe ingresar una opcion del 1 al 5 !")
        continue
    

     # --- OPCIÓN 1: agregar PRODUCTOS ---
    if opcion == 1:
        print("▬▬▬ Agregar producto ▬▬▬")
        nombre = input("Ingrese nombre del producto: ")
        categoria = input("Ingrese la categoría del producto: ")
        precio = int(input("Ingrese el precio del producto (sin centavos): "))

        producto_agregado = [nombre, categoria, precio]
        productos.append(producto_agregado)

        print("\n✅ Producto agregado con éxito!")      
                        
    # --- OPCIÓN 2: MOSTRAR PRODUCTOS ---
    elif opcion == 2:
        print("\n=== LISTA DE PRODUCTOS REGISTRADOS ===")

        if len(productos) == 0:
            print("⚠️ No hay productos registrados aún.")
        else:
            # Enumeramos los productos
            for i in range(len(productos)):
                # accedemos a cada sublista usando el índice i
                nombre = productos[i][0]
                categoria = productos[i][1]
                precio = productos[i][2]

                # i comienza en 0, por eso le sumamos 1 para numerar desde 1
                print(f"{i + 1}. Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")
    
    if opcion == 3:
        print("Buscar producto")
        # Verificamos si hay productos cargados antes de buscar
        if not productos:
            print("⚠️ No hay productos registrados para buscar todavía.")
            continue

        producto_buscado = input("Escriba el producto a buscar: ")
        encontrado = False #indicador

        for i in range(len(productos)):
            nombre = productos[i][0]
            categoria = productos[i][1]
            precio = productos[i][2]

            if producto_buscado == nombre.lower():
                print("\n✅ Producto encontrado:")
                print(f"{i+1}. Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")
                encontrado = True
                break

        if not encontrado:
            print("No existe ese producto.")    
                                        
    if opcion == 4:
        print("Eliminar producto")
        # Verificamos si hay productos cargados antes de buscar
        if not productos:
            print("⚠️ No hay productos registrados!")
            continue

        producto_p_eliminar = input("Escriba el producto para eliminarlo: ").lower()
        encontrado = False #indicador

        for item in productos:
            if producto_p_eliminar.lower() == item[0].lower():                     
                productos.remove(item)
                print(f"El producto {producto_p_eliminar} fue eliminado")
                encontrado = True
                break
        if not encontrado:
            print("No existe ese producto.") 
        
    if opcion == 5:
        print("Saliendo...")
        break
