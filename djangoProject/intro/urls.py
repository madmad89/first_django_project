from django.urls import path

from intro import views

urlpatterns = [
    path('index/', views.hello, name='index'),
    path('list_of_cars/', views.cars, name='list-of-cars'),
    path('list_of_phones/', views.phones, name='list-of-phones'),
]
