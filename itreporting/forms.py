from django import forms
from django.core.mail import send_mail
from itapps.settings import DEFAULT_FROM_EMAIL

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 50)
	email = forms.EmailField()
	subject = forms.CharField(max_length = 100)
	message = forms.CharField(widget = forms.Textarea)

	def send_mail(self):
		send_mail(self.cleaned_data.get('subject') + ', sent on behalf of ' + self.cleaned_data.get('name') + '<' + self.cleaned_data.get('email') + '>', self.cleaned_data.get('message'), DEFAULT_FROM_EMAIL, [DEFAULT_FROM_EMAIL])