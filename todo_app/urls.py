from django.urls import path
from . import views

urlpatterns = [
    path('',views.signin,name="signin"),
    path('register/',views.signup, name="register"),
    path('home/',views.home,name="home"),
    path('update/',views.update,name="update"),
    path('delete/',views.delete,name="delete")
    
]
