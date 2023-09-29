
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name = "create"),
    path('', views.retrieve, name="retrieve"),
    path('edit/<int:stud_id>', views.edit, name="edit"),
    path('update/<int:stud_id>', views.update, name="update"),
    path('delete/<int:stud_id>', views.delete, name="delete"),


]
