from django import forms
from django.contrib import admin

from digital_animals.admin import (
    digital_animal_admin_site, DefaultOrderingModelAdmin
)

from .models import Metadata


class MetadataForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)


@admin.register(Metadata, site=digital_animal_admin_site)
class MetadataAdmin(DefaultOrderingModelAdmin):
    form = MetadataForm
    readonly_fields = ('url_name',)
