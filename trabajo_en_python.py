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

    opcion = int(input("\nSeleccione una opción: ").strip())

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
        nombre = input("Ingrese nombre del producto: ").strip()
        while not nombre:
            print("❌Esta información no puede quedar vacia!")
            nombre = input("Ingrese nombre del producto: ").strip()

        categoria = input("Ingrese la categoría del producto: ").strip()
        while not categoria:
            print("❌Esta información no puede quedar vacia!")
            categoria = input("Ingrese la categoría del producto: ").strip()

        precio = input("Ingrese el precio del producto (sin centavos): ").strip()
        while not precio.isdigit():
            print("❌Esta información no puede quedar vacia o ingresar otro valor que no sean números!")
            precio = input("Ingrese el precio del producto (sin centavos): ").strip()
        precio2 = int(precio)

        producto_agregado = [nombre, categoria, precio2]
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

        producto_buscado = input("Escriba el producto a buscar: ").strip()
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

        # Mostramos la lista numerada
        print("\nLista de productos:")
        for i in range(len(productos)):
            nombre = productos[i][0]
            categoria = productos[i][1]
            precio = productos[i][2]
            print(f"{i + 1}. Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")

        # Pedimos el número del producto a eliminar
        numero = input("\nIngrese el número del producto que desea eliminar: ").strip()

        # Verificamos que no esté vacío y sea numérico
        while not numero.isdigit():
            print("⚠️ Debe ingresar un número válido (solo dígitos).")
            numero = input("Ingrese el número del producto que desea eliminar: ").strip()
    
        numero = int(numero)  # convertimos a entero ahora que sabemos que es válido
    
        # Validamos que el número esté dentro del rango
        if numero < 1 or numero > len(productos):
            print("❌ Número fuera de rango. Intente nuevamente.")
            continue
    
        # Eliminamos el producto seleccionado
        eliminado = productos.pop(numero - 1)
        print(f"\n ❗​❗Producto eliminado correctamente:")
        print(f"   {numero}. Nombre: {eliminado[0]} | Categoría: {eliminado[1]} | Precio: ${eliminado[2]}")
    
    

