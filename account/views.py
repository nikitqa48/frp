from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import *
from django.http import JsonResponse
from rest_framework.response import Response



class ProfileView(CreateAPIView):
    serializer_class = ProfileSerializers


class Fine(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            profile = Profile.objects.get(user = request.user)
            serializer = ProfileSerializers(profile)
            return Response(serializer.data)
        else:
            return Response('Войдите в систему')
    def post(self, request):
        if request.user.is_authenticated:
            profile = request.data.get('User')
            serializer = ProfileSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


