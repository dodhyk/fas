from django.urls import path
from . import views

urlpatterns = [
    path("klub/", views.klub, name='klub'),
    path("klub/input", views.inputklub, name='input-klub'),
    path("klub/edit", views.editklub, name='edit-klub'),
    path("pemain/", views.pemain, name='pemain'),
    path("pemain/input", views.inputpemain, name='input-pemain'),
    path("pemain/edit", views.editpemain, name='edit-pemain'),
    path("liga/", views.liga, name='liga'),
    path("liga/input", views.inputliga, name='input-liga'),
    path("liga/edit", views.editliga, name='edit-liga')
]