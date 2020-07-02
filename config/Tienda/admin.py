from django.contrib import admin
from Tienda.models import Categoria
from Tienda.models import Producto
from Tienda.models import Detalle
from Tienda.models import Venta
from Tienda.models import Direccion
from Tienda.models import Cliente
from Tienda.models import Proveedor


class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['Nombre', ] 
	
    
    list_display = ('RUT', 'Nombre','Telefono')
    

    
 


class ProductoInline(admin.TabularInline):
    model = Producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Precio', 'Stock', 'Categoria', 'Proveedor')
	
    fieldsets = (
		('Descripcion', {
			'fields': ('Nombre',)
			}),
		('Variables',{
			'fields': ('Precio', 'Stock', 'Categoria', 'Proveedor')
			})
	)


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('RUT', 'Nombre','Telefono', 'Web', 'Direccion')
    inlines = [ProductoInline, ] 
	
    list_filter = ('Nombre', 'RUT')	
    

class VentaAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Descuento', 'Cliente', 'MontFin')
    actions = ['valDesc',]

    def valDesc(self,request,queryset):
        return queryset.update(Descuento = True)
    valDesc.short_description = "Validar Descuento"
    

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Descripcion',)    


class DetalleAdmin(admin.ModelAdmin):
    list_display = ('Cantidad', 'Producto',) 


class DireccionAdmin(admin.ModelAdmin):
    list_display = ('Calle', 'Numero', 'Ciudad', 'Comuna') 


# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Detalle, DetalleAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Direccion,DireccionAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
