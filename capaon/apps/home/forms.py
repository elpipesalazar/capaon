from django.contrib.auth.models import User
from django import forms
from capaon.apps.home.models import Empresa, PerfilCliente
from django.utils.translation import ugettext, ugettext_lazy as _
from django.forms.extras.widgets import SelectDateWidget
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.contrib.auth.forms import UserCreationForm

pais = (('Colombia','colombia'), 
		('Venezuela','venezuela'), 
		('Brasil','brasil'))

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')


class EmpresaForm(forms.ModelForm):
	class Meta:
		model = Empresa
	
class UserForm(forms.ModelForm):
	error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
	username = forms.RegexField(label=_("Username"), max_length=30,
		regex=r'^[\w.@+-]+$',
		help_text = _("Required. 30 characters or fewer. Letters, digits and "
			"@/./+/-/_ only."),
		error_messages = {
		'invalid': _("This value may contain only letters, numbers and "
			"@/./+/-/_ characters.")})
	password1 = forms.CharField(label=_("Password"),
		widget=forms.PasswordInput)
	password2 = forms.CharField(label=_("Password confirmation"),
		widget=forms.PasswordInput,
		help_text = _("Enter the same password as above, for verification."))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
		username = self.cleaned_data["username"]
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError(self.error_messages['duplicate_username'])

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1", "")
		password2 = self.cleaned_data["password2"]
		if password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'])
		return password2



class ClienteForm(forms.ModelForm):
    fechaNacimiento = DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    class Meta:
		model = PerfilCliente
		fields = ('cedula','direccion','fechaNacimiento')
		exclude = ('potencial', 'tipo','empresa')



class ContactForm(forms.Form):
	Nombre = forms.CharField(widget = forms.TextInput(attrs = {'class':'input', 'required':'required'}))
	Ciudad = forms.CharField(widget = forms.TextInput(attrs = {'class':'input','required':'required'}))
	Email = forms.EmailField(required=True)
	Mensaje = forms.CharField(widget= forms.Textarea(attrs={'required':'required'}))