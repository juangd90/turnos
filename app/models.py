from django.db import models
from django.db.models.fields import DateField
import datetime
# Create your models here.

dias=(
    ("Lunes","Lunes"),
    ("Martes","Martes"),
    ("Miercoles","Miercoles"),
    ("Jueves","Jueves"),
    ("Viernes","Viernes")
)

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

class Dia(models.Model):
    dia=models.CharField(max_length=64,choices=dias,default="Lunes")
    disponible=models.BooleanField(default=True)

    

    def __str__(self):
        return f"{self.dia}"


class Hora(models.Model):
    horas=models.CharField(max_length=64,choices=horas,default="08:00")
    disponible=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.horas}"


class Turno(models.Model):
    nombre=models.CharField(max_length=64)
    dia=models.ForeignKey(Dia,on_delete=models.CASCADE)
    hora=models.ForeignKey(Hora,on_delete=models.CASCADE)

    def CambiaDisponible(self,dia,hora):
        self.dia.disponible=False
        self.hora.disponible=False
        self.save()

    def __str__(self):
        return f"Turno el día {self.dia} a las {self.hora} para {self.nombre}"
