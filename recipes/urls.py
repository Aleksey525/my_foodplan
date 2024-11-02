from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),
    path('trial_recip_page/', views.trial_recip_page, name='trial_recip_page' )
]