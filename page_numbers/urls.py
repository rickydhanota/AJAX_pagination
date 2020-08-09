from django.urls import path
from . import views
urlpatterns=[
    path('', views.index),
    path('next_table/<int:id>', views.next_table),
    path('change_page/<int:id>', views.change_page),
]