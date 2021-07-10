from rest_framework import serializers
from .models import LibroDiario,boleta,boletaDetalle


class LibroDiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroDiario
        fields = '__all__'

class boletaDetalleSerializers(serializers.ModelSerializer):
    class Meta:
        model = boletaDetalle
        #fields = '__all__'
        fields = ("nombre_producto", "cantidad", "precio_actual")

class boletaSerializer(serializers.ModelSerializer):
    #detalle_boleta = boletaDetalleSerializers()
    detalle = boletaDetalleSerializers(many=True)

    class Meta:
        model = boleta
        fields = '__all__'

    def create(self, validated_data):
        boleta_g = boleta( id_cliente = validated_data.get("id_cliente"),
                           fecha_venta=validated_data.get("fecha_venta"),
                           neto_v = validated_data.get("neto_v"),
                           neto_c=validated_data.get("neto_c"),
                           iva_total=validated_data.get("iva_total"),
                           total_v=validated_data.get("total_v"),
                           metodo_pago = validated_data.get("metodo_pago"),
                         )
        boleta_g.save()
        detalle = validated_data.get('detalle')
        for detalles in detalle:
            boletaDetalle.objects.create(id_boleta=boleta_g, **detalles)
        return validated_data
