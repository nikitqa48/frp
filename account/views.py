from rest_framework.generics import CreateAPIView
from .serializers import *

class ProfileView(CreateAPIView):
    serializer_class = ProfileSerializers


