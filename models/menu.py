# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Inicio'), False, URL('default', 'index'), [])
]


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------


response.menu += [
            (T('Laboratorios'), False, URL('ventas','ventas_productos'), [
                (T('Bagó'), False, URL('ventas', 'venta_productobago'),[]),
                (T('Bayer'), False, URL('ventas', 'venta_productoss'),[]),
                (T('Elea'), False, URL('ventas', 'venta_productoelea'),[]),


        ])]

response.menu += [
                (T('Ampolla'), False, URL('ventas', 'Ampolla'),[
        ])]
response.menu += [

                (T('Blister'), False, URL('ventas', 'Blister'),[

        ])]
response.menu += [
                (T('Crema'), False, URL('ventas', 'Crema'),[

        ])]
response.menu += [
                (T('Efervescente'), False, URL('ventas', 'Efervescente'),[

        ])]
response.menu += [
                (T('Gotas'), False, URL('ventas', 'Gotas'),[

        ])]
response.menu += [
                (T('Grag'), False, URL('ventas', 'Grag'),[

        ])]
response.menu += [
                (T('Jarabe'), False, URL('ventas', 'Jarabe'),[

        ])]
response.menu += [
                (T('Spray'), False, URL('ventas', 'Spray'),[

        ])]
response.menu += [
                (T('Locion'), False, URL('ventas', 'Locion'),[

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

#--------------------------------------------------------------------------------------------------------------
