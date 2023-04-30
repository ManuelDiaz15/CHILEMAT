from django.db import models

# Create your models here.
class clientes(models.Model): # creamos la base de datos con sus atributos
    rut = models.CharField(primary_key=True,max_length=12)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self): #el metodo __str__ es un metodo de python que nos permite mostrar que listar de la base de datos
        texto = "{0}"
        return texto.format(self.nombre)
    
class venta(models.Model):
    codigo_venta = models.CharField(primary_key=True, max_length=50)
    cliente = models.ForeignKey(clientes, on_delete=models.CASCADE, null=False)
    fecha_compra = models.DateField(null=False, blank=True)
    productos = models.CharField(max_length=100)
    
    def __str__(self):
        texto = "{0}"
        return texto.format(self.codigo_venta)