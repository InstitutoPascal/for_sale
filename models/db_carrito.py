# -*- coding: utf-8 -*-


db.define_table ('productos',
                 db.Field("id_producto","id"),
                 #db.Field('id','integer'),
                 db.Field('cantidad_prod','integer',label='Cantidad de Producto'),
                 db.Field ('nombre','string'),
                 db.Field ('laboratorio','string'),
                 db.Field('descripcion','string',label='Descripción'),
                 db.Field('presentacion','string',label='Presentación'),
                 db.Field('cantidad','string'),
                 db.Field('precio','float'),
                 db.Field('proveedor','string'),
                 db.Field('codigo_producto','string'),
                 db.Field('fecha_ingreso','date'),
                 db.Field('numero_remito','integer',label='Número de Remito'),
                 db.Field('numero_lote','integer',label='Número de Lote'),
                 db.Field('imagen','upload'),
                 db.Field('observaciones','text'),
                 db.Field('alicuota_iva','float'),
                 ##fake_migrate=True,
                 )

db.productos.numero_remito.requires=IS_NOT_EMPTY(error_message='***Campo obligatorio***')
db.productos.nombre.requires=IS_NOT_EMPTY(error_message='***Campo obligatorio***')
db.productos.numero_lote.requires=IS_NOT_EMPTY(error_message='***Campo obligatorio***')
db.productos.laboratorio.requires=IS_IN_SET(['Bagó','Bayer','Elea'])
db.productos.presentacion.requires=IS_IN_SET(['Ampolla','Blister','Crema','Efervescente','Gotas','Grag','Jarabe','Spray','Loción'])
db.productos.precio.requires=IS_NOT_EMPTY(error_message='***Campo obligatorio***')
