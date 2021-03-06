"""Turnos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('turnos',views.Turnos,name="turnos"),
    path('reserva',views.reserva,name="reserva"),
    path('busqueda',views.Busqueda,name="busqueda"),
    path('alta_dia',views.AltaDia.as_view(template_name="app/crea_dia.html"),name="alta_dia"),
    path('lista_turnos',views.ListaTurnos.as_view(template_name="app/lista_turnos.html"),name="lista_turnos"),
    path('editar_turno/<int:pk>',views.EditarTurnos.as_view(),name="editar_turno"),
    path('lista_turnos/eliminar/<int:pk>',views.EliminarTurno.as_view(),name="eliminar_turno"),
     path("logout",views.logout_user,name="logout"),
    path("login",views.login_user,name="login")
]
