from django import forms
from django.forms import inlineformset_factory
from .models import Venta, DetalleVenta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['codigo_venta', 'cliente', 'fecha_compra']
        

DetalleVentaFormSet = inlineformset_factory(Venta, DetalleVenta, fields=('producto', 'cantidad'))