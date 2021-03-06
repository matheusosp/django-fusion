from django import forms
from django.core.mail.message import EmailMessage
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=100)
    email = forms.EmailField(label=_('E-mail'), max_length=100)
    subject = forms.CharField(label=_('Subject'), max_length=100)
    message = forms.CharField(label=_('Message'), widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Name:{name}\nEmail:{email}\nsubject:{subject}\nmessage:{message}'

        mail = EmailMessage(
            subject=subject,
            body=content,
            from_email='bremensuporte1@gmail.com',
            to=['bremensuporte1@gmail.com', ],
            headers={'Reply-To': email}
        )
        mail.send()