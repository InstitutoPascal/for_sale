# -*- coding: utf-8 -*-

# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('For sale'), XML('&trade;&nbsp;'), # LOGO SDP
                  _class="navbar-brand", _href="index",
                  _id="web2py-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu_vendedor = [
    (T('For sale'), False, URL('default', 'principal_vendedor'), [])
]


response.menu_vendedor += [
            (T('agregar'), False,  URL('agregar', 'agregar_cliente'),[
                (T('clientes'), False, URL('agregar', 'agregar_cliente'),[])
        ])]

response.menu_vendedor += [
            (T('eliminar'), False, URL('bajas', 'borrar_cliente'),[
                (T('clientes'), False, URL('bajas', 'borrar_cliente'),[])
               
        ])]
               

response.menu_vendedor += [
            (T('reportes'), False, URL('reportes','reportes_productos' ),[
                (T('productos'), False, URL('reportes','reportes_productos' ),[]),
                (T('clientes'), False, URL('reportes','reportes_clientes' ),[])
              ])]
                        
DEVELOPMENT_MENU = True

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------

if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
