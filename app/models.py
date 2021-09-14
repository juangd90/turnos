from django.db import models
from django.db.models.fields import DateField
import datetime

# Create your models here.



horas=(
    ("08:00","08:00"),
    ("08:30","08:30"),
    ("09:00","09:00"),
    ("09:30","09:30"),
    ("10:00","10:00"),
    ("10:30","10:30"),
    ("11:00","11:00"),
    ("11:30","11:30"),

)




class Hora(models.Model):
    horas=models.CharField(max_length=64,choices=horas,default="08:00")
    disponible=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.horas}"
        
class Dia(models.Model):
    dia=models.DateField()
    disponible=models.BooleanField(default=True)
    horario=models.ManyToManyField(Hora)
    
    #hacer metodo para borrar el horario
    def BorraHorario(self,hora):
        horarios=self.horario.all() #traigo todos los horarios disponibles
        for h in horarios: #recorro esos horarios
            if h.horas==hora:# si el horario coincide con lo que recibe por parametro
                self.horario.remove(h)#lo borra de la lista de horarios de ese dia
        self.save()#guarda los cambios   
            

    def __str__(self):
        return f"{self.dia}"

class Turno(models.Model):
    nombre=models.CharField(max_length=64)
    dni=models.IntegerField(max_length=8,default=0)
    dia=models.ForeignKey(Dia,on_delete=models.CASCADE)
    hora=models.ForeignKey(Hora,on_delete=models.CASCADE)   

    def __str__(self):
        return f"Turno el día {self.dia} a las {self.hora} para {self.nombre}"