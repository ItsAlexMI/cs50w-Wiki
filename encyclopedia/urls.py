from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>/', views.entry, name='entry'),
    path('search/', views.search, name='search'),
    path('rand/', views.rand, name='rand'),
    path('create_page/', views.create_page, name='create_page'),
    path('create_page_template/', views.create_page_template, name='create_page_template'),
    path('edit_entry/<str:title>/', views.edit_entry, name='edit_entry'),
    path('eliminate_entry/<str:title>/', views.eliminate_entry, name='eliminate_entry'), 
]
