from django.contrib import admin

from .models import Agenda, HorarioAgenda


class HorarioInline(admin.TabularInline):
    model = HorarioAgenda


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'medico', 'dia']
    inlines = [HorarioInline]
