from django.urls import path, include
from .import views
from .views import BoletaViewset,BoletaDetalleViewset
from rest_framework.routers import  DefaultRouter

router = DefaultRouter()
router.register(r'boleta', BoletaViewset)
router.register(r'boletaDetalle', BoletaDetalleViewset)

urlpatterns = [
    path('', views.LibroDiarioLista, name ="LibroDiario"),
    path('detalle/<str:pk>', views.LibroDiarioDetalle, name ="detalle"),
    path('crear',views.LibroDiarioCrear, name="crear"),
    path('eliminar',views.LibroDiarioEliminar, name="eliminar"),
    path('boleta', views.boletaCrear, name="boleta"),
    path('api/', include(router.urls)),
]