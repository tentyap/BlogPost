
from django.urls import path
from .import views
urlpatterns = [
    path("login",views.LoggingApiView.as_view(),name="login"),
    path("register",views.UserRegisterApiView.as_view(),name="register"),

]