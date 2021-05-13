from django.contrib import admin

from .models import Especialidade


@admin.register(Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
