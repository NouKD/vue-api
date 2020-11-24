from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display =  ('nom', 'prenom', 'age', 'date_add', 'date_update', 'status',)
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom', 'prenom', 'genre', 'phone', 'age', 'email',]}),
        ("standare",{'fields':['status',]})
        ]        


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.User, UserAdmin)
