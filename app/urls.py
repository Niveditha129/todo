from django.urls import path
from app import views
urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('mark_done/<int:pk>/',views.mark_done,name='mark_done'),
    path('mark_notdone/<int:pk>/',views.mark_notdone,name='mark_notdone'),
    path('edit/<int:pk>/',views.edit,name="edit"),
    path('delete/<int:pk>/',views.delete,name="delete")
]
