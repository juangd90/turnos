from django.contrib import admin
from .models import Turno,Dia,Hora
# Register your models here.



admin.site.register(Dia)
admin.site.register(Hora)
admin.site.register(Turno)

