# -*- coding: utf-8 -*-
# try something like

import time
import datetime
from ConfigParser import SafeConfigParser
#response.view = "generic.html"

#forzamos que el usuario se loguee en el sistema
@auth.requires_login()
def VentasLocal():
    #importamos la fecha del sistema
    import time
    #obtengo la fecha 
    fecha_dia= time.strftime("%x")
    #guardo la fecha en la sesion
    session["fecha_actual"]=fecha_dia
    #obtenemos el id del usuario logeado en el sistema y en base a ese obtengo los campos del usuario
    usuario_log = db(db.empleados.usuario_id == auth.user_id ).select().first()
    #extraigo del usuario logueado el nombre 
    vendedor_log = usuario_log.nombre
    #agrego el usuario logueado en la sesion
    session["vendedor_log"] = vendedor_log
    #obtenemos de la tabla clientes los siguientes campos, el id, el nombre y el codigo del cliente
    campos = db.clientes.id, db.clientes.nombre, db.clientes.codigo_cliente
    #defino la condición que deben cumplir los datos que se obtendran de la base de datos
    criterio = db.clientes.id>0
    #ejecutamos la consulta utilizando el criterio y utilizando los campos previamente obtenidos 
    lista_clientes = db(criterio).select(*campos)
    #revisar si la consulta devolvio registros
    if not lista_clientes:
        mensaje = "No ha cargado clientes"
    else:
        mensaje = "Seleccione un cliente"
    #redirije los valores al HTML
    return dict(message=mensaje, lista_clientes=lista_clientes, vendedor_log=vendedor_log, fecha_dia=fecha_dia, )

def Borrar_Item():
    #eliminar el elemento de la lista en posicion pos x
    del session["items_venta"][int(request.vars.pos)]
    return dict()

def CancelarVenta():
    #elimina todos los elementos de la lista (diccionario) items_venta
    del session["items_venta"]
    return dict()

def VentasLocalCarga():
    #importamos la fecha del sistema
    import time
    #verificamos si la vista nos devuelve un nombre
    if "id_cliente" in request.vars:
        session["id_cliente"] = request.vars["id_cliente"]  # traer del form y guardo en la sesion
    cliente = db(db.clientes.id == session["id_cliente"] ).select().first() #enbase al id del cliente obtenido de la sesion, obtengo los datos del mismo
    cliente_venta = cliente.nombre
    #verifico si presiono el boton =boton_enviar (agregar producto) en el formulario, continuo
    if request.vars["boton_enviar"]:
        #obtengo el id del cliente del formulario web en la vista VentasLocal
        id_cliente = request.vars["id_cliente"]
        usuario_actual  = request.vars.userlog
        #guardo el id de cliente en la sesión
        session["id_cliente"] = id_cliente
        #Defino en la sesion que inicie una lista (diccionario) en blanco
        session["items_venta"] = []
        #verifico si presionaron el boton =agregar_item en el formulario web, continuo.
    if request.vars["agregar_item"]:
        # obtengo los valores del formulario
        codigo_barras = request.vars["id_producto"]
        #verifico si el codigo de barras ingresado no esta en la base, envia un mensaje de error
        if db(db.productos.codigo_barras==codigo_barras).count()==0: #este count cuenta los registros y si es == a 0 muestra el error
            response.flash = 'El codigo de barras ingresado no esta en la base de datos'
        else:
            # busco en la base de datos el codigo de barras ingresado, lo comparo y obtengo los campos de la tabla productos
            reg_producto = db(db.productos.codigo_barras==codigo_barras).select().first()
            # obtengo el id de la consulta anterior
            id_producto = reg_producto.id_producto
            # obtengo la candidad de productos ingresado en el formulario
            cantidad = request.vars["cantidad"]
            # creo un diccionario y lo inicializo con el id y la cantidad de producto
            item = {"id_producto": id_producto, "cantidad": int(cantidad)}
            # agrego nuevos registros en el diccionario (item["nombredelaclave"] = variablequetraelaconsulta.campodelatablaconsultada)
            item["nombre"] = reg_producto.nombre
            item["marca"] = reg_producto.marca
            item["descripcion"] = reg_producto.descripcion
            item["precio"] = reg_producto.precio
            item["alicuota_iva"] = reg_producto.alicuota_iva
            #guardo el item en la sesión
            session["items_venta"].append(item)
    return dict( fecha_dia=session["fecha_actual"], items_venta=session["items_venta"], cliente_venta=cliente_venta, vend=session["vendedor_log"],)
        
def confirmar():
    total = 0
    #Obtengo el los datos del cliente en base al id obtenido de la sesion
    cliente = db(db.clientes.id == session["id_cliente"] ).select().first()
    cliente_venta = cliente.nombre
    #Recorro lo almacenado en items_venta en la session y hago los calculos de los impuesto para enviarlos a la vista de confirmacion de la venta
    for item in session["items_venta"]:
        total += (item["precio"] * item["cantidad"] + item["precio"] * item["cantidad"] *item["alicuota_iva"]/100.00)
    return dict (cliente_venta=cliente_venta, fecha_dia=session["fecha_actual"], total=total, vend=session["vendedor_log"])
