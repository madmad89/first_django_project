from django.urls import path

from home import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home_page'),
    path('get_data/', views.get_data_by_emag, name='get-data'),
    ]
