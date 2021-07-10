from django.db import models
from django.utils import timezone

# Create your models here.

class LibroDiario(models.Model):
    id_transaccion = models.CharField(max_length=100, default= 'DEFAULT VALUE')
    nombre_transaccion = models.CharField(max_length=100, default= 'DEFAULT VALUE')
    debe = models.CharField(max_length=50, default= 'DEFAULT VALUE')
    haber = models.CharField(max_length=50, default= 'DEFAULT VALUE')
    fecha = models.DateField(auto_now_add=True)


    class Meta:
        db_table = 'libroDiario'

    def __str__(self):
        return  self.nombre_transaccion

class boleta(models.Model):
    #id = models.AutoField(primary_key=True)
    id_cliente = models.IntegerField()
    fecha_venta = models.DateField(auto_now_add=False)
    neto_v = models.IntegerField(default=0)
    neto_c = models.IntegerField(default=0)
    iva_total = models.IntegerField(default=0)
    total_v = models.IntegerField(default=0)
    metodo_pago = models.CharField(max_length=10, default='DEFAULT VALUE')  ## EFECTIVO 1 DEBITO 2  CREDITO 3

    class Meta:
        db_table = 'Boleta'

    def __int__(self):
        return  self.id

class boletaDetalle(models.Model):

    id_boleta = models.ForeignKey(boleta, on_delete=models.CASCADE,related_name='detalle')
    nombre_producto = models.CharField(max_length=100)
    cantidad = models.IntegerField(default=0)
    precio_actual = models.IntegerField(default=0)
    class Meta:
        db_table = 'boletaDetalle'

    def __int__(self):
        return  self.id

