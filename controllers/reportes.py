# -*- coding: utf-8 -*-
# intente algo como

def reportes_clientes():
    subtitulo=T('Listado de Clientes')
    listado =db(db.clientes).select(db.clientes.ALL)
    return dict(dc=listado)
#----------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
#reportes por productos
def reportes_productos():
    subtitulo=T('Listado de Productos')
    listado =db(db.productos).select(db.productos.ALL)
    return dict(dc=listado)

#------------------------------------------------------------------------------------------------------------------------------------------------------------#Reportes de empleados

def reportes_vendedor():
    subtitulo=T('Listado de Empleados')
    listado =db(db.vendedor).select(db.vendedor.ALL)
    return dict(dc=listado)
