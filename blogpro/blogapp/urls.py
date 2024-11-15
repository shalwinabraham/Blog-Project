from django.urls import path,include
from .views import*

urlpatterns = [
    path('',Tasklistview.as_view(),name="list"),
    path('detial/<int:pk>',Taskdetialview.as_view(),name="detail"),
    path('create/',Taskcreateview.as_view(),name ="create" ),
    path('update/<int:pk>',Taskupdateview.as_view(),name ="update" ),
    path('delete/<int:pk>',Taskdeleteview.as_view(),name ="delete" )
]