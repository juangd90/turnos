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
        dia_seleccionado=request.POST.get('fecha')#trae la fecha seleccionada
        dia,created=Dia.objects.get_or_create(dia=dia_seleccionado)
        horas=dia.horario.all()
        #horas=request.POST.get('horas')
        nombre=request.POST.get('nombre')
        dni=request.POST.get('dni')
        #prueba,created=Dia.objects.get_or_create(dia=dia)
        #hora,created=Hora.objects.get_or_create(horas=horas)
        #prueba.BorraHorario("11:00")
        #turno=Turno(nombre=nombre,dni=12345678,dia=prueba,hora=hora)
        #turno.save()
        return render(request,"app/reservas.html",{
          'dia':dia,
          'horas':horas,
          'nombre':nombre,
          'dni':dni
        })
    else:
        primer_dia=Dia.objects.first()
        ultimo_dia=Dia.objects.last()     
            
        
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

        


