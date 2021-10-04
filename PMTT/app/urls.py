from django.urls import path
from .import views 

urlpatterns = [
    path('Base/', views.Base ,name='Base'),
    path('dashboard/', views.dashboard ,name='dashboard'),
    path('testing/', views.testing ,name='testing'),
    path('allprojects/', views.allprojects ,name='allprojects'),
    path('calendar/', views.calendar ,name='calendar'),
    path('conference/', views.conference ,name='conference'),
    path('cost/', views.cost ,name='cost'),
    path('createproject/', views.createproject ,name='createproject'),
    path('datavisual/', views.datavisual ,name='datavisual'),
    path('discussion/', views.discussion ,name='discussion'),
    path('login/', views.login,name='login'),
    path('profile/', views.profile ,name='profile'),
    path('reportcreation/', views.reportcreation ,name='reportcreation'),
    path('risk/', views.risk ,name='risk'),
    path('skillgap/', views.skillgap ,name='skillgap'),
    path('task/', views.task ,name='task'),
 
]