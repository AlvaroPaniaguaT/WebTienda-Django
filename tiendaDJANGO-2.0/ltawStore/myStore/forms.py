from django import forms
from django.utils.safestring import mark_safe


CHOICES = [(1, mark_safe('<img src="https://cdn.pccomponentes.com/img/footer/proceso-pago/visa.png"></img>')),
		   (2, mark_safe('<img src="https://cdn.pccomponentes.com/img/footer/proceso-pago/maestro.png"></img>')),
		   (3, mark_safe('<img src="https://cdn.pccomponentes.com/img/footer/proceso-pago/master.png"></img>')),
		   (4, mark_safe('<img src="https://cdn.pccomponentes.com/img/footer/proceso-pago/dolar.png"></img>'))]

class PaymentForm(forms.Form):
	payMeth = forms.ChoiceField(label='Metodo de pago',required=True, widget=forms.RadioSelect(), choices=CHOICES)
	quantity = forms.IntegerField(label='Cantidad', required=True)
	full_name = forms.CharField(label='Nombre completo',required=True, max_length=200)
	email_address = forms.CharField(label='E-Mail', required=True, max_length=200, widget=forms.EmailInput())
	country = forms.CharField(label='Pais', required=True, max_length=200)
	city = forms.CharField(label='Ciudad', required=True, max_length=200)
	address = forms.CharField(label='Direccion', required=True, max_length=200)
	aditional_comments = forms.CharField(label='Comentarios', required=True, max_length=200, widget=forms.Textarea())

class PaymentFormCart(forms.Form):
	payMeth = forms.ChoiceField(label='Metodo de pago',required=True, widget=forms.RadioSelect(), choices=CHOICES)
	full_name = forms.CharField(label='Nombre completo',required=True, max_length=200)
	email_address = forms.CharField(label='E-Mail', required=True, max_length=200, widget=forms.EmailInput())
	country = forms.CharField(label='Pais', required=True, max_length=200)
	city = forms.CharField(label='Ciudad', required=True, max_length=200)
	address = forms.CharField(label='Direccion', required=True, max_length=200)
	aditional_comments = forms.CharField(label='Comentarios', required=True, max_length=200, widget=forms.Textarea())