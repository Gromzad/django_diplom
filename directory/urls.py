from django.urls import path
from .views import *

app_name = 'directory'
urlpatterns = [
    path('', directory, name='home'),
    path('s/', search, name='пошук'),
    path('metalproduction/', metalproduction, name='Вироби металургійного виробництва'),
    path('machinebuild/', machinebuild, name='Вироби машинобудівного виробництва'),
    path('instrproduction/', instrproduction, name='Вироби інструментального виробництва'),
    path('carbuild/', carbuild, name='Вироби автомобілебудівного виробництва'),
    path('traktorbuild/', traktorbuild, name='Вироби тракторного та сільсьскогосподарського машинобудування'),
    path('chembuild/', chembuild, name='Вироби хімічного машинобудування'),
    path('metalproduction/<str:slug>', metalproductionPost, name='metalproductionPost'),
    path('machinebuild/<str:slug>', machinebuildPost, name='machinebuildPost'),
    path('instrproduction/<str:slug>', instrproductionPost, name='instrproductionPost'),
    path('carbuild/<str:slug>', carbuildPost, name='carbuildPost'),
    path('traktorbuild/<str:slug>', traktorbuildPost, name='traktorbuildPost'),
    path('chembuild/<str:slug>', chembuildPost, name='chembuildPost'),
]
