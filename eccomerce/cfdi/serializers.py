from rest_framework import serializers
from cfdi.models import Cfdi

class CreateCfdiSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		return Cfdi.objects.create(**validated_data)

	class Meta:
		model = Cfdi
		fields = (
			'journail_id', 
			'currendy_id', 
			'payment_method_id',
			'estado_pago', 
			'forma_pago',
			'payment_type',
			'tipocambio',
			'total_factura',
			'tax_payment',
			'monedaDR',
			'equivalenciaDR',
			'folio_facura',
			'IdDocumento',
			'numParcialidad',
			'ImpSaldoAnt',
			'ImpPagado',
			'ImpSaldoInsoluto',
			'ObjetoImpDr',
			'ImpuestoDR',
			'factura_cfdi',
			'monto_pagado',
			'payment_content')

	

class CfdiSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cfdi
		fields = (
			'journail_id', 
			'currendy_id', 
			'payment_method_id',
			'estado_pago', 
			'forma_pago',
			'payment_type',
			'tipocambio',
			'total_factura',
			'tax_payment',
			'monedaDR',
			'equivalenciaDR',
			'folio_facura',
			'IdDocumento',
			'numParcialidad',
			'ImpSaldoAnt',
			'ImpPagado',
			'ImpSaldoInsoluto',
			'ObjetoImpDr',
			'ImpuestoDR',
			'factura_cfdi',
			'monto_pagado',
			'payment_content')