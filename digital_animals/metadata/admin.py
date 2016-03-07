from django.contrib import admin

from digital_animals.admin import (
    digital_animal_admin_site, DefaultOrderingModelAdmin
)

from .models import Metadata


@admin.register(Metadata, site=digital_animal_admin_site)
class MetadataAdmin(DefaultOrderingModelAdmin):
    readonly_fields = ('url_name',)
