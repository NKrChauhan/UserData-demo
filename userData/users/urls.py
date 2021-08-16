from django.urls import path
from .views import editUserinfoAPI,listUserinfoAPI,detailUserinfoAPI

urlpatterns = [
    path('api/list/',listUserinfoAPI,name='list'),
    path('api/edit/<uid>/',editUserinfoAPI,name='edit'),
    path('api/detail/<uid>/',detailUserinfoAPI,name='detail'),
]
