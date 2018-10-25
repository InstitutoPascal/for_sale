# -*- coding: utf-8 -*-
# intente algo como

def borrar_cliente():
    # obtengo el primer argumento (ver URL)
    id_cliente = request.args[0]
    # busco y borro el registro
    db(db.clientes.id == id_clientes).delete()
    session.flash = "El cliente %s se borro exitosamente" % id_clientes
    # redirijo al usuario al listado
    redirect(URL(c="reportes", f="reportes_clientes"))

def borrar_vendedor():
    # obtengo el primer argumento (ver URL)
    id_vendedor = request.args[0]
    # busco y borro el registro
    db(db.vendedor.id == id_vendedor).delete()
    session.flash = "El vendedor %s se borro exitosamente" % id_vendedor
    # redirijo al usuario al listado
    redirect(URL(c="reportes", f="reportes_vendedor"))

def borrar_producto():
    # obtengo el primer argumento (ver URL)
    id_producto = request.args[0]
    # busco y borro el registro
    db(db.productos.id == id_producto).delete()
    session.flash = "El producto %s se borro exitosamente" % id_producto
    # redirijo al usuario al listado
    redirect(URL(c="reportes", f="reportes_productos"))
