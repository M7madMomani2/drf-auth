from django.shortcuts import render
from .serializers import AuthSerializers
from .models import Auth
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.
class AuthList(ListCreateAPIView):
    queryset = Auth.objects.all()
    serializer_class = AuthSerializers

class AuthDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Auth.objects.all()
    serializer_class = AuthSerializers

