"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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


from personas.views import detallePersona, nuevaPersona, BorrarPersona, editarPersona
from Webapp.views import Bienvenido
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Bienvenido/', Bienvenido,name = 'inicio'),
    path('detalle_persona/<int:id>',detallePersona),
    path('nueva_persona/', nuevaPersona,name='nuevo'),
    path('Eliminar_persona/<int:id>',BorrarPersona, name= 'borrar'),
    path('Editar_persona/<int:id>',editarPersona, name = 'editar'),

]

