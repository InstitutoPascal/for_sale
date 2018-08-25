# -*- coding: utf-8 -*-

db.define_table ('productos',
                 db.Field("id_producto","id"),  #agregada by enrique
                 #db.Field('id','integer'),
                 db.Field('codigo_barras', 'string'),
                 db.Field('cantidad_prod','integer'),
                 db.Field ('nombre','string'),
                 db.Field ('marca','string'),
                 db.Field('descripcion','string'),
                 db.Field('envase','string'),
                 db.Field ('categoria','string'),
                 db.Field('precio','float'),
                 db.Field('proveedor','string'),
                 db.Field ('codigo_producto','string'),
                 db.Field ('fecha_ingreso','string'),
                 db.Field('numero_remito','integer'),
                 db.Field('numero_lote','integer'),
                 db.Field('imagen','upload'),
                 db.Field('observaciones','text'),
                 db.Field('alicuota_iva','float') #agregada by enrique
                 )
