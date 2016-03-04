from django import forms
from django.utils.translation import ugettext_lazy as _


class OrderForm(forms.Form):
    name = forms.CharField(
        min_length=3, max_length=250,
    )
    email = forms.EmailField(max_length=254,)
    phone = forms.CharField(
        required=False, max_length=19,
    )
    message = forms.CharField(
        min_length=5, max_length=500, widget=forms.Textarea,
    )

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        self.fields['name'].label = _('Имя')
        self.fields['name'].widget.attrs = {
            'placeholder': _('Введите имя'),
            'data-rule-required': 'true',
            'data-msg-required': _(
                'Мы все еще не знаем как к вам обращаться'
            ),
        }

        self.fields['email'].label = _('E-mail')
        self.fields['email'].widget.attrs = {
            'placeholder': _('Введите почтовый адрес'),
            'data-rule-required': 'true',
            'data-msg-required': _(
                'Мы все еще не знаем как к вам обращаться'
            ),
            'data-rule-email': 'true',
            'data-msg-email': _(
                'Странный адрес, что-то с ним не так'
            ),
        }

        self.fields['phone'].label = _('Телефон')
        self.fields['phone'].widget.attrs = {
            'placeholder': _('Введите номер телефона'),
            'data-rule-required': 'true',
            'data-msg-required': _(
                'Мы все еще не знаем как к вам дозвониться'
            ),
            'data-mask': '+380 (99) 999-9999',
        }

        self.fields['message'].widget.attrs = {
            'placeholder': _('Введите сообщение'),
            'data-rule-required': 'true',
            'data-msg-required': _(
                'Мы не знаем что вам ответить на это'
            ),
        }
