from django.contrib import admin
from .models import LibroDiario, boleta, boletaDetalle


# Register your models here.

admin.site.register(LibroDiario)
admin.site.register(boleta)
admin.site.register(boletaDetalle)
