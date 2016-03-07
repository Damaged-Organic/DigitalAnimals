from django.contrib import admin

from digital_animals.admin import (
    digital_animal_admin_site, DefaultOrderingModelAdmin
)

from .models import (
    Benefit, Feature, Step, Pricing, Contact
)


@admin.register(Benefit, site=digital_animal_admin_site)
class BenefitAdmin(DefaultOrderingModelAdmin):
    readonly_fields = ('icon',)


@admin.register(Feature, site=digital_animal_admin_site)
class FeatureAdmin(DefaultOrderingModelAdmin):
    ordering = ('id',)
    readonly_fields = ('image',)


@admin.register(Step, site=digital_animal_admin_site)
class StepAdmin(DefaultOrderingModelAdmin):
    ordering = ('id',)
    readonly_fields = ('icon',)


@admin.register(Pricing, site=digital_animal_admin_site)
class PricingAdmin(DefaultOrderingModelAdmin):
    ordering = ('id',)


@admin.register(Contact, site=digital_animal_admin_site)
class ContactAdmin(DefaultOrderingModelAdmin):
    ordering = ('id',)
