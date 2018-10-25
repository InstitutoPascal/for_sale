# -*- coding: utf-8 -*-

def venta_productos():

    subtitulo=T('Ingrese el nombre del medicamento a buscar:')
    tablaFinal=[]
    i=0
    form2=''
    # buscar todos los productos:
    condicion = db.productos.laboratorio
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos, orderby= db.productos.nombre)#ordenar alfabeticamente

    # vista generica para pruebas:
    #response.view = "generic.html"
    return dict(registros=registros)

def venta_productoss():

    # buscar todos los productos:
    condicion = db.productos.laboratorio == 'Bayer'
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos, orderby= db.productos.nombre)#ordenar alfabeticamente

    # vista generica para pruebas:
    #response.view = "generic.html"
    return dict(registros=registros)

def venta_productoelea():

    # buscar todos los productos:
    condicion = db.productos.laboratorio == 'Elea'
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos, orderby= db.productos.nombre)#ordenar alfabeticamente

    # vista generica para pruebas:
    #response.view = "generic.html"
    return dict(registros=registros)

def venta_productobago():

    # buscar todos los productos:
    condicion = db.productos.laboratorio == 'Bagó'
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos, orderby= db.productos.nombre)#ordenar alfabeticamente

    # vista generica para pruebas:
    #response.view = "generic.html"
    return dict(registros=registros)


def Blister():
    # buscar todos los productos:
    condicion = db.productos.presentacion =='Blister'
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos, orderby= db.productos.nombre)#ordenar alfabeticamente

    # vista generica para pruebas:
    #response.view = "generic.html"
    return dict(registros=registros)

def Crema():
    # buscar todos los productos:
    condicion = db.productos.presentacion =='Crema'
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos, orderby= db.productos.nombre)#ordenar alfabeticamente

    # vista generica para pruebas:
    #response.view = "generic.html"
    return dict(registros=registros)

def Ampolla():
    # buscar todos los productos:
    condicion = db.productos.presentacion =='Ampolla'
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos, orderby= db.productos.nombre)#ordenar alfabeticamente

    # vista generica para pruebas:
    #response.view = "generic.html"
    return dict(registros=registros)

def Efervescente():
    # buscar todos los productos:
    condicion = db.productos.presentacion =='Efervescente'
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos, orderby= db.productos.nombre)#ordenar alfabeticamente

    # vista generica para pruebas:
    #response.view = "generic.html"
    return dict(registros=registros)

def Gotas():
    # buscar todos los productos:
    condicion = db.productos.presentacion =='Gotas'
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos, orderby= db.productos.nombre)#ordenar alfabeticamente

    # vista generica para pruebas:
    #response.view = "generic.html"
    return dict(registros=registros)

def Grag():
    # buscar todos los productos:
    condicion = db.productos.presentacion =='Grag'
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos, orderby= db.productos.nombre)#ordenar alfabeticamente

    # vista generica para pruebas:
    #response.view = "generic.html"
    return dict(registros=registros)

def Jarabe():
    # buscar todos los productos:
    condicion = db.productos.presentacion =='Jarabe'
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos, orderby= db.productos.nombre)#ordenar alfabeticamente

    # vista generica para pruebas:
    #response.view = "generic.html"
    return dict(registros=registros)

def Spray():
    # buscar todos los productos:
    condicion = db.productos.presentacion =='Spray'
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos, orderby= db.productos.nombre)#ordenar alfabeticamente

    # vista generica para pruebas:
    #response.view = "generic.html"
    return dict(registros=registros)

def Locion():
    # buscar todos los productos:
    condicion = db.productos.presentacion =='Loción'
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos, orderby= db.productos.nombre)#ordenar alfabeticamente

    # vista generica para pruebas:
    #response.view = "generic.html"
    return dict(registros=registros)

def carrito():
      # obtengo los valores del formulario
    if request.vars["producto"]:
        id_prod = request.vars["producto"]
        cantidad = request.vars["cantidad"]
        print "este es el id", id_prod
        # revisar que request.vars.codigo cumpla con las validaciones
        #session.codigo_barras = request.vars.id_producto
        # buscamos el producto en la base datos
        #cantidad = request.vars["cantidad"]
        item = {"id_producto": id_prod, "cantidad": int(cantidad)}
        # busco en la base de datos el registro del producto seleccionado
        reg_producto = db(db.productos.id_producto==id_prod).select().first()
        item["descripcion"] = reg_producto.nombre
        item["precio"] = reg_producto.precio
        item["alicuota_iva"] = reg_producto.alicuota_iva
        # si no está definida la lista de items, lo creamos vacia en la sesión:
        if "items_venta" not in session:
            session["items_venta"] = []
        # guardo el item en la sesión
        session["items_venta"].append(item)
        #print"usuario ",session["vendedor_logueado"]
    return dict(items_venta=session["items_venta"])
    

def confirmar():
    #reg_cliente = db(db.clientes.id==session["id_cliente"]).select().first()
    total = 0
    for item in session["items_venta"]:
        total += (item["precio"] * item["cantidad"] + item["precio"] * item["cantidad"] *item["alicuota_iva"]/100.00)
    return dict (mensaje= "Finalizar venta", total=total)

def borrar_item():
    # eliminar el elemento de la lista en posicion pos
    del session["items_venta"][int(request.vars.pos)]
    return dict()

def mostrar():
    # obtengo el id de prodcuto desde la URL
    prod_id = request.args[0]
    # consultamos a la bd para que traiga el registro del primer producto:
    reg = db(db.productos.id_producto==prod_id).select(db.productos.imagen).first()
    # obtenemos la imagen (nombre de archivo completo, stream=flujo de datos=archivo abierto -open-):
    (filename, stream) = db.productos.imagen.retrieve(reg.imagen)
    # obtenemos extension original para determinar tipo de contenido:
    import os.path
    ext = os.path.splitext(filename)[1].lower()
    if ext in (".jpg", ".jpeg", ".face"):
        formato = "image/jpeg"
    elif ext in (".png"):
        formato = "image/png"
    response.headers['Content-Type'] = formato
    # devolver al navegador el contenido de la image
    return stream

def productos():

    #buscar todos los productos:
    condicion = db.productos.laboratorio
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos)

    #vista generica para pruebas:
    #response.view = "generic.html"
    return dict(registros=registros)

def cancelar_venta():
    del session["items_venta"]
    return dict()

def nombres():
    # buscar todos los productos:
    condicion = db.productos.nombre
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos, orderby= db.productos.nombre)#ordenar alfabeticamente

    # vista generica para pruebas:
    #response.view = "generic.html"
    return dict(registros=registros)
