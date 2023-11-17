from django.urls import include, path
from . import views 

urlpatterns = [
    path('user',views.user, name='user'),
    #path('viewuser',views.viewalluser, name='viewuser'),
    path('view',views.viewall, name='view'),
    path('add',views.add, name='add'),
    path('search',views.search, name='search'),  
    path('delete',views.delete, name='delete'),
]