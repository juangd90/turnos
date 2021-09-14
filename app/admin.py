from django.contrib import admin
from .models import Turno,Dia,Hora
# Register your models here.
class DiaAdmin(admin.ModelAdmin):
    list_display=("dia","disponible")


admin.site.register(Dia,DiaAdmin)
admin.site.register(Hora)
admin.site.register(Turno)

