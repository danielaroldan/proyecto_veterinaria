from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
# class Usuario(models.Model):
# nombre = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    contraseña = models.CharField(max_length=15)


class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    razonSocialCliente = models.CharField(max_length=200)
    direccionCliente = models.CharField(max_length=200)
    localidadCliente = models.CharField(max_length=200)
    provinciaCliente = models.CharField(max_length=200)
    codigoPostalCliente = models.CharField(max_length=10)
    telefonoCliente = models.CharField(max_length=20)
    ivaCliente = models.BooleanField()
    mailCliente = models.CharField(max_length=200)
    fechaCreacionCliente = models.DateTimeField(default=timezone.now)
    fechaModificaciónCliente = models.DateTimeField(default=timezone.now)
    fechaBajaCliente = models.DateTimeField(default=timezone.now)


class Articulo(models.Model):
    articulo = models.AutoField(primary_key=True)
    codigoArticulo = models.IntegerField()
    precioArticulo = models.IntegerField()
    detalleArticulo = models.CharField(max_length=200)


class StockArticulo(models.Model):
    stockArticulo = models.OneToOneField(Articulo, on_delete=models.CASCADE,
                                         default=None)
    entradaStock = models.IntegerField()
    salidaStock = models.IntegerField()
    stockArticulo = models.IntegerField()
    fechaCreacion = models.DateTimeField(default=timezone.now)
    fechaModificación = models.DateTimeField(default=timezone.now)
    fechaBaja = models.DateTimeField(default=timezone.now)


class Venta(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name='cliente')
    cantidadUnitarioArticulo = models.OneToOneField(
        StockArticulo, on_delete=models.CASCADE, related_name='stock_artic')
    cantidadTotalArticulo = models.IntegerField()
    precioUnitarioArticulo = models.IntegerField()
    fechaVenta = models.DateTimeField(default=timezone.now)


class Factura(models.Model):
    fechaFactura = models.DateTimeField(default=timezone.now)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name='factura')
    venta = models.OneToOneField(Venta, on_delete=models.CASCADE,
                                 default=Venta)
    articulo = models.ForeignKey(
        Articulo, on_delete=models.CASCADE, related_name='aticulo')
    precioUnitarioArticulo = models.DecimalField(
        max_digits=8, decimal_places=2)
    precioTotalArticulo = models.DecimalField(max_digits=8, decimal_places=2)
    iva = models.DecimalField(max_digits=8, decimal_places=2)

    def publish(self):
        self.nombre = timezone.now()
        self.save()


def __str__(self):
    return self.idCliente
