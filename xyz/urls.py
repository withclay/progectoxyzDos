from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from xyz.views import Inicio
from usuario_rol.views import Login, LogoutUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(Inicio), name='index'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout/', login_required(LogoutUsuario), name='logout')
]
