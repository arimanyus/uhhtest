from django.urls import path
from . import views

app_name = 'sites'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list_sites, name='list_sites'),
    path('new_website/', views.website_form_view, name='new_website'),
    path('detail/<int:website_id>/',
         views.website_detail,
         name='website_detail'),  # new line
]
