from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response



class ProfileView(CreateAPIView):
    serializer_class = ProfileSerializers


@api_view(['GET', 'POST'])
def hello(request):
    if request.method == 'GET':
        if request.user.is_authenticated:

            profile = Profile.objects.get(user = request.user)
            print(profile.phone)
            context = {
                profile: 'profile'
            }
            return Response (context)
        else:
            print('НЕ АВТОРИЗИРОВАН')