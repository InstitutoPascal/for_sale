# -*- coding: utf-8 -*-

# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('SDP'), XML('&trade;&nbsp;'), # LOGO SDP
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

response.menu_supervisor = [
    (T('Home'), False, URL('default', 'index'), [])
]


response.menu_supervisor += [
    (T('Altas'), False, '#', [
    
            (T('Tipos de Empleo'), False,
             URL('altas', 'altas_Categorias')),

            (T('Estudios'), False,
             URL('altas', 'altas_Estudios')), 
            
            (T('Estudios por Empleo'), False,
             URL('altas', 'altas_exe')), 
            
                            ])
                ]

response.menu_supervisor += [
    (T('Bajas'), False, '#', [
    
            (T('Tipos de Empleo'), False,
             URL('bajas', 'listaCategorias')),

            (T('Estudios'), False,
             URL('bajas', 'listaEstudios')), 
                            ])
                ]

response.menu_supervisor += [
    (T('Modificaciones'), False, '#', [
    
            (T('Tipos de Empleo'), False,
             URL('modificaciones', 'listaCategorias')),

            (T('Estudios'), False,
             URL('modificaciones', 'listaEstudios')), 
                            ])
                ]

response.menu_supervisor += [
    (T('Reportes'), False, '#', [
    
            (T('Tipos de Empleo'), False,
             URL('reportes', 'listaCategorias')),

            (T('Estudios'), False,
             URL('reportes', 'estudios')), 
            
            (T('Estudios por Empleo'), False,
             URL('reportes', 'listaempleos')), 
            
                            ])
                ]


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
