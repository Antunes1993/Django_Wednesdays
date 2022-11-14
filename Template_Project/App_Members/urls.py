from django.urls import path 
from . import views

urlpatterns = [
    # PATH CONVERTERS
    # int numbers
    # str strings 
    # path whole urls /
    # slug hyphen-and_underscores_stuff
    # UUID universally unique identifier

    path('login_user', views.login_user, name="login_user"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('register_user', views.register_user, name="register_user"),

]
