from django.urls import path
from .views import AuthList,AuthDetail

urlpatterns = [
    path('',AuthList.as_view(),name='auth_list'),
    path('<int:pk>/',AuthDetail.as_view(),name='auth_detail')
]