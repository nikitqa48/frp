from rest_framework.generics import CreateAPIView
from .serializers import *

class ProfileView(CreateAPIView):
    serializer_class = ProfileSerializers()

class ModelView(CreateAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializers(many=True)
