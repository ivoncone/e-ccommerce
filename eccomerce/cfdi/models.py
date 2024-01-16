from django.db import models

class Cfdi(models.Model):
	journail_id = models.IntegerField(null=True, blank=True)
	currendy_id = models.IntegerField(null=True, blank=True)
	payment_method_id = models.IntegerField(null=True, blank=True)
	estado_pago = models.CharField(max_length=250, null=True, blank=True)
	forma_pago = models.CharField(max_length=500)
	payment_type = models.CharField(max_length=500, null=True, blank=True)
	tipocambio = models.FloatField(null=True, blank=True)
	total_factura = models.FloatField(null=True, blank=True)
	tax_payment = models.TextField(max_length=500)
	monedaDR = models.CharField(max_length=500)
	equivalenciaDR = models.CharField(max_length=500)
	folio_facura = models.CharField(max_length=500)
	IdDocumento = models.CharField(max_length=500)
	numParcialidad = models.CharField(max_length=500)
	ImpSaldoAnt = models.FloatField(null=True, blank=True)
	ImpPagado = models.FloatField(null=True, blank=True)
	ImpSaldoInsoluto = models.FloatField(null=True, blank=True)
	ObjetoImpDr = models.CharField(max_length=500)
	ImpuestoDR = models.TextField()
	factura_cfdi = models.BooleanField(null=True, blank=True)
	monto_pagado = models.FloatField(null=True, blank=True)
	payment_content = models.TextField()

	def __str__(self):
		return self.name 

	class Meta:
		db_table = 'cfdi'