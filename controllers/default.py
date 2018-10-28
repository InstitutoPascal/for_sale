# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    
    nombre_rol='SIN ROL'  #ingresa sin rol
    if auth.user_id:  #variable que contiene el id del usuario logueado
        reg_id_grupo_del_logueado=db(auth.user.id==db.auth_membership.user_id).select(db.auth_membership.group_id)
        id_grupo_del_logueado=reg_id_grupo_del_logueado[0].group_id  #esta variable contiene el id del grupo, es decir solo el número (limpiamos la variable anterior)
        reg_nombre_rol=db(db.auth_group.id==id_grupo_del_logueado).select(db.auth_group.role)
        nombre_rol=reg_nombre_rol[0].role #limpiamos variable anterior para que solo busque el rol (la palabra)
        # se asigna un rol
        
        if nombre_rol=='Administrador':
            redirect(URL('principal_administrador'))
        elif nombre_rol=='vendedor':
            redirect(URL('principal_vendedor'))
        else:
            redirect(URL('principal_cliente'))

    response.flash = T("For sale")    
    return dict(message=T('Bienvenido al Sistema de ventas online'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def principal_cliente():
    return dict ()

@auth.requires_membership(role='administrador')
def principal_administrador():
    return dict ()

@auth.requires_membership(role='vendedor')
def principal_vendedor():
    return dict ()
