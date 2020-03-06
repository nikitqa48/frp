from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from project.models import *

class OrganisationAdressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Organisation_adress
        fields = ['site', 'legal_address', 'actual_address', 'correspondence']

class OrganisationSerializers(serializers.ModelSerializer):
    address = OrganisationAdressSerializers()
    class Meta:
        model = Organisation
        fields = ['full_name',
                  'short_name',
                  'ogrn',
                  'kpp', 'data_registration', 'chef',
                  'contact', 'target',
                  'address',
                  ]

class ProfileSerializers(UserCreateSerializer):
    organisation = OrganisationSerializers()
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'organisation', 'phone']



