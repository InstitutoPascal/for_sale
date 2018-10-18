# -*- coding: utf-8 -*-

# intente algo como
def index(): return dict(message="hello from altasUsuarios.py")

def altasCliente():
    subtitulo=T('Listado de Usuarios Registrados Pendientes de Aprobación - Sistema de Datos Preocupacionales')#Asigna mensaje a mostrar
    nombre=auth.user.first_name
    apellido=auth.user.last_name
    registrados = db(db.auth_user.registration_key == 'pending').select(db.auth_user.ALL)
    return dict(subtitulo=subtitulo, nombre=nombre, apellido=apellido, registrados=registrados)

def agregarVendedor():
    subtitulo=T('Listado de Usuarios Registrados Pendientes de Aprobación - Sistema de Datos Preocupacionales')#Asigna mensaje a mostrar
    nombre=auth.user.first_name
    apellido=auth.user.last_name
    
    grupoElegido=db(request.args(1)==db.auth_group.role).select(db.auth_group.id)
    for x in grupoElegido:
        clave=x.id
    cd = db.auth_membership.insert(user_id=request.args(0) , group_id=clave)#AGREGA UN REGISTRO
    
    usuario=db(request.args(0)==db.auth_user.id).select(db.auth_user.ALL)
    reg=usuario[0]
    reg.update_record(registration_key='')#AUTORIZA AL NUEVO USUARIO A USAR EL SISTEMA (QUITA 'pending')

    redirect(URL('altasVendedor'))

    return dict(subtitulo=subtitulo, nombre=nombre, apellido=apellido , cd=cd )


def eliminarRegistrado():
    db(db.auth_user.id==request.args(0)).delete()
    redirect(URL('altasSupervisores'))
    return dict ()

def ejemclientes():
    form = SQLFORM(db.clientes)
    if form.process().accepted:
        response.flash = 'formulario aceptado'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)
