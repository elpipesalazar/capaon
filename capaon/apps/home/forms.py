from django import forms
from capaon.apps.home.models import Empresa

pais = (('Colombia','colombia'), 
		('Venezuela','venezuela'), 
		('Brasil','brasil'))


class EmpresaForm(forms.Form):
	Nombre = forms.CharField(widget = forms.TextInput(attrs = {'required':'required'}))
	NIT = forms.CharField(widget = forms.TextInput(attrs = {'required':'required'}))
	Direccion = forms.CharField(widget = forms.TextInput(attrs = {'required':'required'}))
	Actividad = forms.CharField(widget = forms.TextInput(attrs = {'required':'required'}))
	Telefono = forms.CharField(widget = forms.TextInput(attrs = {'required':'required','type':'tel'}))
	Fax = forms.DecimalField(widget = forms.TextInput(attrs = {'required':'required'}))
	Email = forms.EmailField(required=True)
	Pais = forms.CharField(widget = forms.Select(choices=pais))

class IndividualForm(forms.Form):
	Nombre = forms.CharField(widget = forms.TextInput(attrs = {'required':'required'}))
	Apellido = forms.CharField(widget = forms.TextInput(attrs = {'required':'required'}))
	Cedula = forms.CharField(widget = forms.TextInput(attrs = {'required':'required'}))
	Direccion = forms.CharField(widget = forms.TextInput(attrs = {'required':'required'}))
	FechaNacimiento = forms.DateField(widget = forms.TextInput(attrs = {'required':'required','type':'date'}))
	Telefono = forms.CharField(widget = forms.TextInput(attrs = {'required':'required'}))
	Celular = forms.CharField(widget = forms.TextInput(attrs = {'required':'required'}))
	Email = forms.EmailField(required=True)
	Pais = forms.CharField(widget = forms.Select(choices=pais))


class ContactForm(forms.Form):
	Nombre = forms.CharField(widget = forms.TextInput(attrs = {'class':'input', 'required':'required'}))
	Ciudad = forms.CharField(widget = forms.TextInput(attrs = {'class':'input','required':'required'}))
	Email = forms.EmailField(required=True)
	Mensaje = forms.CharField(widget= forms.Textarea(attrs={'required':'required'}))