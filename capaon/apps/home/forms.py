from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext, ugettext_lazy as _
from capaon.apps.home.models import Empresa, PerfilCliente
from django.forms.extras.widgets import SelectDateWidget
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField

pais = (('Colombia','colombia'), 
		('Venezuela','venezuela'), 
		('Brasil','brasil'))


class EmpresaForm(ModelForm):
	class Meta:
		model = Empresa
		exclude = ('representante',)
	


class ClienteForm(ModelForm):
	username        = forms.CharField(label=_('Nickname'))
	nombre          = forms.CharField(label=(u'Nombre'))
	apellidos       = forms.CharField(label=(u'Apellidos'))
	email           = forms.EmailField(label=(u'Email'))
	password        = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput(render_value=False))
	password1       = forms.CharField(label=_(u'Password confirmation'), widget=forms.PasswordInput(render_value=False))
	fechaNacimiento = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',)) 
	error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }

	class Meta:
		model = PerfilCliente
		fields = ('username','password','password1','nombre','apellidos','email','cedula','direccion','telefono','celular','fechaNacimiento','ciudad','pais')
		exclude = ('potencial', 'tipo','empresa')

	def clean_username(self):
                username = self.cleaned_data['username']
                try:
                        User.objects.get(username=username)
                except User.DoesNotExist:
                        return username
                raise forms.ValidationError(self.error_messages['duplicate_username'])

	def clean(self):
            if self.cleaned_data['password'] != self.cleaned_data['password1']:
                    raise forms.ValidationError(self.error_messages['password_mismatch'])
            return self.cleaned_data



class ContactForm(forms.Form):
	Nombre = forms.CharField(widget = forms.TextInput(attrs = {'class':'input', 'required':'required'}))
	Ciudad = forms.CharField(widget = forms.TextInput(attrs = {'class':'input','required':'required'}))
	Email = forms.EmailField(required=True)
	Mensaje = forms.CharField(widget= forms.Textarea(attrs={'required':'required'}))