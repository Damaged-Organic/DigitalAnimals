from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin


class DigitalAnimalAdminSite(admin.AdminSite):
    site_title = 'Digital Animals'
    site_header = 'Deus Ex Machina'
    index_title = 'Digital Animals Administration'

digital_animal_admin_site = DigitalAnimalAdminSite(name='deus_ex_machina')


class DefaultOrderingModelAdmin(admin.ModelAdmin):
    ordering = ('id',)


@admin.register(Group, site=digital_animal_admin_site)
class GroupAdmin(GroupAdmin):
    pass


@admin.register(User, site=digital_animal_admin_site)
class UserAdmin(UserAdmin):
    pass
