from django.urls import path
from . import views

urlpatterns = [
    path('base',views.base),
    path('home',views.home,name='home'),
    path('form',views.form,name='form'),
    path('form',views.form,name='form'),
    path('delete/<pk>',views.delete,name='delete'),
    path('edit/<pk>',views.edit,name='edit'),
    path('',views.login_data,name='login'),
    path('logout',views.logout_data,name='logout'),
]
