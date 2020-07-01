from django.db import models

# Create your models here.

class Direccion(models.Model):
    Calle = models.CharField(max_length=50)
    Numero = models.IntegerField()
    Ciudad = models.CharField(max_length=50)
    Comuna = models.CharField(max_length=50)

    def __str__(self):
        return "Direccion: " + str(self.Calle) + " " + str(self.Numero) + " " + str(self.Ciudad) + " " + str(self.Comuna)

class Proveedor(models.Model):
    RUT = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    Direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    Web = models.CharField(max_length=50)

    def __str__(self):
        return "Proveedor: " + str(self.RUT) + " " + str(self.Nombre) + " " + str(self.Telefono) + " " + str(self.Direccion) + " " + str(self.Web)   

class Categoria(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=100)

    def __str__(self):
        return "Categoria: " + str(self.ID) + " " + str(self.Nombre)+ " " + str(self.Descripcion)


class Producto(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Precio = models.IntegerField()
    Stock = models.IntegerField()
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return "Producto: " + str(self.ID) + " " + str(self.Nombre) + " " + str(self.Precio) + " " + str(self.Stock) + " " + str(self.Categoria) + " " + str(self.Proveedor)


class Detalle(models.Model):
    Cantidad = models.IntegerField()
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return "Detalle: " + str(self.Cantidad) + " " + str(self.Producto)


class Venta(models.Model):
    ID = models.AutoField(primary_key=True)
    Fecha = models.CharField(max_length=50)
    Descuento = models.IntegerField()
    MontoFinal = models.IntegerField()
    Detalle = models.ForeignKey(Detalle, on_delete=models.CASCADE)

    def __str__(self):
        return "Venta: " + str(self.ID) + " " + str(self.Fecha) + " " + str(self.Descuento) + " " + str(self.MontoFinal) + " " + str(self.Detalle)        


        
class Cliente(models.Model):
    RUT = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    Direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    Venta = models.ForeignKey(Venta, on_delete=models.CASCADE)

    def __str__(self):
        return "Cliente: " + str(self.RUT) + " " + str(self.Nombre) + " " + str(self.Telefono) + " " + str(self.Direccion) + " " + str(self.Venta)   


