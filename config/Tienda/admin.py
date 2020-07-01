from django.contrib import admin
from Tienda.models import Categoria
from Tienda.models import Producto
from Tienda.models import Detalle
from Tienda.models import Venta
from Tienda.models import Direccion
from Tienda.models import Cliente
from Tienda.models import Proveedor





# Register your models here.
admin.site.register(Categoria,)
admin.site.register(Producto,)
admin.site.register(Detalle,)
admin.site.register(Venta, )
admin.site.register(Direccion,)
admin.site.register(Cliente,)
admin.site.register(Proveedor,)
