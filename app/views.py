from django.db.models import fields
from django.shortcuts import render, redirect
from .models import Turno, Dia,Hora
import datetime
from django.urls.base import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
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
        #trae fecha, nombre y dni para empezar el proceso de reserva de turno
        return render(request,"app/reservas.html",{
          'dia':dia,
          'horas':horas,
          'nombre':nombre,
          'dni':dni,
         #pasa esa info a reservas para que se continue con el proceso
        })
    else:
        primer_dia=Dia.objects.order_by('dia').first()       
        ultimo_dia=Dia.objects.order_by('dia').last()         
          #paso primer y ultimo dia para armar el calendario  
        
        return render(request,"app/turnos.html",{
            'primer_dia':primer_dia,
            'ultimo_dia':ultimo_dia,         
             
            
        })

def reserva(request): #aca traigo toda la info que completa y confirma el usuario para generar la reserva del turno
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        dni=request.POST.get('dni')
        horas=request.POST.get('horas')
        hora,created=Hora.objects.get_or_create(horas=horas)
        fecha=request.POST.get('dia')
        dia,created=Dia.objects.get_or_create(dia=fecha)
        turno=Turno(nombre=nombre,dni=dni,dia=dia,hora=hora)
        turno.save()
        dia.BorraHorario(horas)#luego de generado el turno, borro el horario asociado a ese dia
        return render(request,"app/index.html",{
            
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


class AltaDia(LoginRequiredMixin,CreateView):
    login_url='login'
    model=Dia
    form=Dia
    fields="__all__"
    success_url=reverse_lazy('index')    

        
class ListaTurnos(LoginRequiredMixin,ListView):
    login_url='login'
    model=Turno
    form=Turno
    fields="__all__"
    success_url=reverse_lazy('index') 

class EditarTurnos(LoginRequiredMixin,UpdateView):
    login_url='login'
    model=Turno
    form=Turno
    fields="__all__"
    template_name="app/editar_turno.html"
    success_url=reverse_lazy('lista_turnos') 

class EliminarTurno(LoginRequiredMixin,DeleteView):
    login_url='login'
    model=Turno
    form=Turno
    fields="__all__"    
    success_url=reverse_lazy('lista_turnos') 

def logout_user(request):
    logout(request)
    return redirect("index") 

def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
       context={}
       return render(request,'app/login.html',context) 