from django.contrib import admin
from .models import Usuario,TipoUsuario,atencion, registroMascota


# Register your models here.
admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(atencion)
admin.site.register(registroMascota)