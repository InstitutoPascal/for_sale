# -*- coding: utf-8 -*-
# try something like

def productos():
    form = SQLFORM(db.productos)
    if form.process().accepted:
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Por favor complete el formulario'
    return dict(form=form)
