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

def Turnos(request):
    if request.method=='POST':
        dia=request.POST.get('fecha')#trae la fecha seleccionada
        horas=request.POST.get('horas')
        nombre=request.POST.get('nombre')
        prueba,created=Dia.objects.get_or_create(dia=dia)
        hora,created=Hora.objects.get_or_create(horas=horas)
        #prueba.BorraHorario("11:00")
        turno=Turno(nombre=nombre,dni=12345678,dia=prueba,hora=hora)
        turno.save()
        return render(request,"app/index.html",{
            'turno':turno
        })
    else:
        primer_dia=Dia.objects.first()
        ultimo_dia=Dia.objects.last()
        horas=Hora.objects.filter(disponible=True)
        turno=Turno.objects.all()
        
        return render(request,"app/turnos.html",{
            'primer_dia':primer_dia,
            'ultimo_dia':ultimo_dia,
            'horas':horas,
            'turno':turno,
            
        })



