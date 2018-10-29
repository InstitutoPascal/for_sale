# -*- coding: utf-8 -*-
# try something like

def producto_nombre():
    subtitulo=T('Ingrese el nombre del medicamento')
    tablaFinal=[]
    i=0
    form2=''

    form=FORM(TABLE(TR("",INPUT(_type="text",_name="nombre",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar",_class="btn btn-primary"))))#construlle el formulario para la vista, submit (tipo boton)
    if form.accepts(request.vars,session):
        ### verifica si la carrera estÃ¡ en la base de datos
        if db(db.productos.nombre==form.vars.nombre).count()==0: #este count cuenta los registros y si es == a 0 muestra el error
            form.errors.codigo="El el nombre del medicamento no esta en la base de datos"
            response.flash = 'El el nombre del medicamento no esta en la base de datos'
        else:
          
            listado =db(db.productos.nombre==form.vars.nombre).select(db.productos.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('NOMBRE',_style='width:150px; color:#FF0000; background: #eef; border: 2px solid #cdcdcd'),TH('PRECIO',_style='width:150px; color:#FF0000 background: #eef; border: 2px solid #cdcdcd'),
            *[TR(TD(x.nombre,_style='width:150px; color:#FF0000 background: #eef; border: 2px solid #cdcdcd'),
            TD(x.precio,_style='width:150px; color:#FF0000 background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            
            
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)

def reportes_productos():
    subtitulo=T('Listado de Productos')
    listado =db(db.productos).select(db.productos.ALL)
    return dict(dc=listado)

def reportes_clientes():
    subtitulo=T('Listado de Clientes')
    listado =db(db.clientes).select(db.clientes.ALL)
    return dict(dc=listado)

def reportes_vendedor():
    subtitulo=T('Listado de Clientes')
    listado =db(db.vendedor).select(db.vendedor.ALL)
    return dict(dc=listado)
