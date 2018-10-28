# -*- coding: utf-8 -*-
# try something like

def borrar_cliente():
    # obtengo el primer argumento (ver URL)
    id_cliente = request.args[0]
    # busco y borro el registro
    db(db.clientes.id == id_clientes).delete()
    session.flash = "El cliente %s se borro exitosamente" % id_clientes
    # redirijo al usuario al listado
    redirect(URL(c="reportes", f="reportes_clientes"))

    
def borrar_productos():
    # obtengo el primer argumento (ver URL)
    id_productos = request.args[0]
    # busco y borro el registro
    db(db.productos.id == id_productos).delete()
    session.flash = "El producto %s se borro exitosamente" % id_productos
    # redirijo al usuario al listado
    redirect(URL(c="reportes", f="reportes_productos"))

def borrar_vendedor():
    # obtengo el primer argumento (ver URL)
    id_vendedor= request.args[0]
    # busco y borro el registro
    db(db.vendedor.id == id_vendedor).delete()
    session.flash = "El empleado %s se borro exitosamente" % id_vendedor
    # redirijo al usuario al listado
    redirect(URL(c="reportes", f="reportes_vendedor"))
