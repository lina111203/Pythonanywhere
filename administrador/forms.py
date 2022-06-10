from dataclasses import field
from django import forms
from administrador.models import Electrodomestico,Elemento, Factura, Marca, Servicio, Tipos_Elemento, Usuario,Stock
from administrador.models import Electrodomestico,Elemento, Marca, Servicio, Tipos_Elemento
from usuarios.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rol','Unombre','apellido','tipo_documento','documento','celular']
           
class TipoElementoForm(forms.ModelForm):
    class Meta:
        model= Tipos_Elemento
        fields=['categoria','subcategoria']
        
class TipoElementoEditarForm(forms.ModelForm):
    class Meta:
        model= Tipos_Elemento
        fields=['categoria','subcategoria']
        
class ElementoForm(forms.ModelForm):
    class Meta:
        model= Elemento
        fields= ['tipo_elemento','nombre','marca','descripcion','precio','porcentaje_ganancia', 'foto']

class ElementoEditarForm(forms.ModelForm):
    class Meta:
        model= Elemento
        fields= ['tipo_elemento','nombre','marca' ,'descripcion','precio','porcentaje_ganancia', 'foto']
                
class MarcaForm(forms.ModelForm):
    class Meta:
        model= Marca
        fields= ['nombre']
        
class MarcaEditarForm(forms.ModelForm):
    class Meta:
        model= Marca
        fields= ['nombre']
        
# class FacturaForm(forms.ModelForm):
#     class Meta:
#         model= Factura
#         fields= ['elemento','cantidad','compraoventa','usuario', 'monto', 'fecha']
        
# class FacturaEditarForm(forms.ModelForm):
#     class Meta:
#         model= Factura
#         fields= ['elemento','cantidad','compraoventa','usuario', 'monto', 'fecha']

class ElectrodomesticoForm(forms.ModelForm):
    class Meta:
        model= Electrodomestico
        fields=['nombre', 'marca', 'referencia']

class ElectrodomesticoEditarForm(forms.ModelForm):
    class Meta:
        model= Electrodomestico
        fields=['nombre', 'marca', 'referencia']
        
class ServicioForm(forms.ModelForm):
    class Meta:
        model= Servicio
        fields=['electrodomestico','diagnostico', 'tiposervicio', 'cantidad', 'fallas_basicas','fecha_entrega']

class ServicioEditarForm(forms.ModelForm):
    class Meta:
        model= Servicio
        fields=['electrodomestico','diagnostico', 'tiposervicio', 'cantidad', 'fallas_basicas','fecha_entrega']
class StockForm(forms.ModelForm):
    class Meta:
        model= Stock
        fields=['stock_stock']