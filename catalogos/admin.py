from django.contrib import admin

from django.contrib.auth.models import Group, User
from .models import Area, Sexo, Carrera, Laboratorio, Modalidad, Turno, Asignatura,\
 Marca, Modelo, Color, Estado

admin.site.site_header='Registro Laboratorio'



admin.site.register(Area)
admin.site.register(Sexo)
admin.site.register(Carrera)
admin.site.register(Laboratorio)
admin.site.register(Modalidad)
admin.site.register(Turno)
admin.site.register(Asignatura)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Color)
admin.site.register(Estado)
# Register your models here.
