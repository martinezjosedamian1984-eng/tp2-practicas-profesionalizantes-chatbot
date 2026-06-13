#cerebro - sistemas experto
productos = [
    {"nombre": "Mouse", "categoria": "Periféricos", "stock": 3, "precio": 5000},
    {"nombre": "Teclado", "categoria": "Periféricos", "stock": 4, "precio": 9000},
    {"nombre": "Monitor", "categoria": "Pantallas", "stock": 8, "precio": 120000},
    {"nombre": "Notebook", "categoria": "Computadoras", "stock": 2, "precio": 750000}
]



#                   parameatro
def sistema_experto(mensaje):
    mensaje = mensaje.lower()
    hechos = []
    #detectar los hechos escritos por el usuario
    if "hola" in mensaje:
        hechos.append("saludo")
    if "adios" in mensaje or "chao" in mensaje:
        hechos.append("despedida")
    if "saludo" in hechos:
        return "¡Hola! ¿En qué puedo ayudarte?"
    
    if "despedida" in hechos:
        return "¡Antes de despedirnos quisiera saber si hay algo más en lo que te pueda ayudar! 👋"
    if "stock bajo" in mensaje or "productos con bajo stock" in mensaje:
        productos_bajo_stock = []

        for producto in productos:
            if producto["stock"] <= 5:
                productos_bajo_stock.append(producto)

        respuesta = "Productos con stock bajo:<br>"

        for producto in productos_bajo_stock:
            respuesta += f"- {producto['nombre']} | stock: {producto['stock']}<br>"

        return respuesta
    
    if "productos mas caros" in mensaje or "productos más caros" in mensaje or "mas caros" in mensaje or "más caros" in mensaje:
        productos_ordenados = sorted(productos, key=lambda producto: producto["precio"], reverse=True)

        respuesta = "Productos más caros:<br>"

        for producto in productos_ordenados:
            respuesta += f"- {producto['nombre']} | precio: ${producto['precio']}<br>"

        return respuesta
    
    if "stock por categoria" in mensaje or "stock por categoría" in mensaje or "stock total por categoria" in mensaje or "stock total por categoría" in mensaje:
        stock_categorias = {}

        for producto in productos:
            categoria = producto["categoria"]
            stock = producto["stock"]

            if categoria in stock_categorias:
                stock_categorias[categoria] += stock
            else:
                stock_categorias[categoria] = stock

        respuesta = "Stock total por categoría:<br>"

        for categoria, stock_total in stock_categorias.items():
            respuesta += f"- {categoria} | stock total: {stock_total}<br>"

        return respuesta
    
    if "resumen general" in mensaje or "resumen" in mensaje or "informe general" in mensaje:
        total_productos = len(productos)
        stock_total = 0
        cantidad_bajo_stock = 0
        producto_mas_caro = productos[0]

        for producto in productos:
            stock_total += producto["stock"]

            if producto["stock"] <= 5:
                cantidad_bajo_stock += 1

            if producto["precio"] > producto_mas_caro["precio"]:
                producto_mas_caro = producto

        respuesta = "Resumen general:<br>"
        respuesta += f"- Total de productos: {total_productos}<br>"
        respuesta += f"- Stock total: {stock_total}<br>"
        respuesta += f"- Producto más caro: {producto_mas_caro['nombre']} | ${producto_mas_caro['precio']}<br>"
        respuesta += f"- Productos con stock bajo: {cantidad_bajo_stock}<br>"

        return respuesta
    if "recomendar reposicion" in mensaje or "recomendar reposición" in mensaje or "reponer stock" in mensaje or "que productos repongo" in mensaje:
        productos_a_reponer = []

        for producto in productos:
            if producto["stock"] <= 5:
                productos_a_reponer.append(producto)

        productos_a_reponer = sorted(
            productos_a_reponer,
            key=lambda producto: producto["stock"]
        )

        respuesta = "Productos recomendados para reponer:<br>"

        for producto in productos_a_reponer:
            respuesta += f"- {producto['nombre']} | stock: {producto['stock']}<br>"

        return respuesta
    if "ayuda" in mensaje or "comandos" in mensaje or "que podes hacer" in mensaje or "qué podés hacer" in mensaje:
        respuesta = "Puedo ayudarte con estas consultas:<br>"
        respuesta += "- productos con stock bajo<br>"
        respuesta += "- productos más caros<br>"
        respuesta += "- stock total por categoría<br>"
        respuesta += "- resumen general<br>"
        respuesta += "- reponer stock<br>"

        return respuesta
    
    if "estado del negocio" in mensaje or "estado negocio" in mensaje or "como esta el negocio" in mensaje or "cómo está el negocio" in mensaje:
        productos_bajo_stock = []
        stock_categorias = {}
        producto_mas_caro = productos[0]

        for producto in productos:
            # 1) Detectar productos con stock bajo
            if producto["stock"] <= 5:
                productos_bajo_stock.append(producto)

            # 2) Sumar stock por categoría
            categoria = producto["categoria"]
            stock = producto["stock"]

            if categoria in stock_categorias:
                stock_categorias[categoria] += stock
            else:
                stock_categorias[categoria] = stock

            # 3) Buscar producto más caro
            if producto["precio"] > producto_mas_caro["precio"]:
                producto_mas_caro = producto

        # 4) Producto más urgente para reponer
        producto_urgente = sorted(
            productos_bajo_stock,
            key=lambda producto: producto["stock"]
        )[0]

        # 5) Categoría con mayor stock
        categoria_mayor_stock = max(
            stock_categorias,
            key=stock_categorias.get
        )

        respuesta = "Estado del negocio:<br>"
        respuesta += f"- Hay {len(productos_bajo_stock)} productos con stock bajo.<br>"
        respuesta += f"- Producto más urgente para reponer: {producto_urgente['nombre']} | stock: {producto_urgente['stock']}<br>"
        respuesta += f"- Categoría con mayor stock: {categoria_mayor_stock} | stock total: {stock_categorias[categoria_mayor_stock]}<br>"
        respuesta += f"- Producto más caro: {producto_mas_caro['nombre']} | ${producto_mas_caro['precio']}<br>"

        return respuesta
    #respuesta por defecto del sistema
    return "Disfruto poder ayudarte con tus dudas y acompañarte y hacer tus gestiones más sencillas."