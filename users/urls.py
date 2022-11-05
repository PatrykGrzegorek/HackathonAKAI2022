from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    # url(r'^', include(router.urls)),
    path('login', views.LoginView),

    path('children/registration', views.RegistrationChildren.as_view(), name="create"),
    path('children/<id>/', views.OneChildrenView),
    path('addcash/<id>/', views.AddCash),
]
