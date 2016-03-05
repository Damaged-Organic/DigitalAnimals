from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail


class OrderForm(forms.Form):
    name = forms.CharField(
        min_length=3, max_length=250,
    )
    email = forms.EmailField(max_length=254,)
    phone = forms.CharField(
        max_length=19,
    )
    message = forms.CharField(
        min_length=5, max_length=500, widget=forms.Textarea,
    )

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        # Name
        self.fields['name'].label = _('order.name.label')
        self.fields['name'].widget.attrs = {
            'placeholder': _('order.name.placeholder'),
            'data-rule-required': 'true',
            'data-msg-required': _('error_messages.name.required'),
            'data-rule-minlength': 3,
            'data-msg-minlength': _('error_messages.name.min_length'),
            'data-rule-maxlength': 250,
            'data-msg-maxlength': _('error_messages.name.max_length'),
        }
        self.fields['name'].error_messages = {
            'required': _('error_messages.name.required'),
            'min_length': _('error_messages.name.min_length'),
            'max_length': _('error_messages.name.max_length'),
        }

        # E-mail
        self.fields['email'].label = _('order.email.label')
        self.fields['email'].widget.attrs = {
            'placeholder': _('order.email.placeholder'),
            'data-rule-required': 'true',
            'data-msg-required': _('error_messages.email.required'),
            'data-rule-email': 'true',
            'data-msg-email': _('error_messages.email.invalid'),
            'data-rule-maxlength': 254,
            'data-msg-maxlength': _('error_messages.email.max_length'),
        }
        self.fields['email'].error_messages = {
            'required': _('error_messages.email.required'),
            'invalid': _('error_messages.email.invalid'),
            'max_length': _('error_messages.email.max_length'),
        }

        # Phone
        self.fields['phone'].label = _('order.phone.label')
        self.fields['phone'].widget.attrs = {
            'placeholder': _('order.phone.placeholder'),
            'data-rule-required': 'true',
            'data-msg-required': _('error_messages.phone.required'),
            'data-rule-maxlength': 19,
            'data-msg-maxlength': _('error_messages.phone.max_length'),
            'data-mask': '+380 (99) 999-9999',
        }
        self.fields['phone'].error_messages = {
            'required': _('error_messages.phone.required'),
            'max_length': _('error_messages.phone.max_length'),
        }

        # Message
        self.fields['message'].widget.attrs = {
            'placeholder': _('order.message.placeholder'),
            'data-rule-required': 'true',
            'data-msg-required': _('error_messages.message.required'),
            'data-rule-minlength': 5,
            'data-msg-minlength': _('error_messages.message.min_length'),
            'data-rule-maxlength': 500,
            'data-msg-maxlength': _('error_messages.message.max_length'),
        }
        self.fields['message'].error_messages = {
            'required': _('error_messages.message.required'),
            'min_length': _('error_messages.message.min_length'),
            'max_length': _('error_messages.message.max_length'),
        }

    def send_email(self):
        send_mail(
            'Subject',
            ''.join([
                self.cleaned_data['message'],
                ' ',
                self.cleaned_data['email'],
                ' ',
                self.cleaned_data['phone']
            ]),
            'webmaster@cheers-development.in.ua',
            ['webmaster@cheers-development.in.ua'],
            fail_silently=False
        )

"""
from django.core.mail import send_mail
from django.template.loader import render_to_string


msg_plain = render_to_string('templates/email.txt', {'some_params': some_params})
msg_html = render_to_string('templates/email.html', {'some_params': some_params})

send_mail(
    'email title',
    msg_plain,
    'some@sender.com',
    ['some@receiver.com'],
    html_message=msg_html,
)
"""
