from django.shortcuts import render
from .models import Turno, Dia,Hora
from django.views.generic import ListView, CreateView
from django.urls.base import reverse_lazy
# Create your views here.

def index(request):
    return render(request,'app/index.html')

'''class Turnos(CreateView):
    model=Turno
    form=Turno
    fields="__all__"
    success_url=reverse_lazy('index') '''
#hay que traer los dias y horarios disponibles, y en base a eso mostrar el calendario
#ademas tiene que recibir la fecha y hora elegida y con eso cambiar el estado disponible a false
# con el get_or_create
def Turnos(request):
    if request.method=='POST':
        ...
    else:
        dias=Dia.objects.filter(disponible=True)
        horas=Hora.objects.filter(disponible=True)
        return render(request,"app/turnos.html",{
            'dias':dias,
            'horas':horas,
        })



