"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from tasks import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import os


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('carrito/', views.carrito, name='carrito'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('plus-cart/', views.plus_cart, name='plus_cart'),
    path('minus-cart/', views.minus_cart, name='minus_cart'),
    path('remove-cart/', views.remove_cart, name='remove_cart'),
    path('vaciar-carrito/', views.vaciar_carrito, name='vaciar_carrito'),
    path('perfil/', views.perfil, name='perfil'),
    path('checkout/', views.checkout, name='checkout'),
    path('pago-exitoso/<int:pedido_id>/', views.pago_exitoso, name='pago_exitoso'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Configuración para servir archivos media tanto en desarrollo como en producción
if settings.DEBUG:
    # En desarrollo, Django puede servir archivos media directamente
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # En producción, necesitamos configurar manualmente la URL para archivos media
    # Esta configuración trabajará con la estructura de carpetas propuesta 
    # (media dentro de staticfiles)
    urlpatterns += [
        path('media/<path:path>', serve, {
            'document_root': os.path.join(settings.BASE_DIR, 'media'),
        }),
    ]