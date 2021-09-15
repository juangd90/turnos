from django.db.models import fields
from django.shortcuts import render
from .models import Turno, Dia,Hora
import datetime
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def index(request):
    return render(request,'app/index.html')


def Turnos(request):
    if request.method=='POST':
        dia_seleccionado=request.POST.get('fecha')#trae la fecha seleccionada
        dia,created=Dia.objects.get_or_create(dia=dia_seleccionado)
        horas=dia.horario.all()        
        nombre=request.POST.get('nombre')
        dni=request.POST.get('dni')     
        
        return render(request,"app/reservas.html",{
          'dia':dia,
          'horas':horas,
          'nombre':nombre,
          'dni':dni,
         
        })
    else:
        primer_dia=Dia.objects.order_by('dia').first()       
        ultimo_dia=Dia.objects.order_by('dia').last()
          
            
        
        return render(request,"app/turnos.html",{
            'primer_dia':primer_dia,
            'ultimo_dia':ultimo_dia,         
             
            
        })

def reserva(request):
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        dni=request.POST.get('dni')
        horas=request.POST.get('horas')
        hora,created=Hora.objects.get_or_create(horas=horas)
        fecha=request.POST.get('dia')
        dia,created=Dia.objects.get_or_create(dia=fecha)
        turno=Turno(nombre=nombre,dni=dni,dia=dia,hora=hora)
        turno.save()
        dia.BorraHorario(horas)

        return render(request,"app/index.html",{
            'nombre':nombre
        })
    else:
        return render(request,"app/turnos.html")

def Busqueda(request):
    if request.method=='POST':
        dni=request.POST.get('dni')
        turnos_list=Turno.objects.filter(dni=dni)
        return render(request,"app/resultados.html",{
            'turnos_list':turnos_list,
        })
    else:
        return render(request,"app/busca_turno.html")    


class AltaDia(CreateView):
    model=Dia
    form=Dia
    fields="__all__"
    success_url=reverse_lazy('index')    

        
class ListaTurnos(ListView):
    model=Turno
    form=Turno
    fields="__all__"
    success_url=reverse_lazy('index') 

