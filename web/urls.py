from django.urls import path
from .import views
from .views import home, librodiario

#app_name='web'
urlpatterns = [
    path('', home, name="home"),
    path('librodiario/', librodiario, name="librodiario"),

]