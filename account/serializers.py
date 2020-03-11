from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from project.models import *
from account.models import *

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
                  'inn',
                  'address',
                  ]


class UserSerializers(UserCreateSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']


class ProfileSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    organisation = OrganisationSerializers()

    class Meta:
        model = Profile
        fields = ['user', 'organisation', 'phone']

    def create(self, validated_data):
        data = validated_data
        user_data = data['user']
        organisation_data = data['organisation']
        organisation_address = organisation_data['address']
        object_address = Organisation_adress.objects.create(
                site=organisation_address['site'],
                legal_address=organisation_address['legal_address'],
                actual_address=organisation_address['actual_address'],
                correspondence=organisation_address['correspondence']
        )
        organisation = Organisation.objects.create(full_name=organisation_data['full_name'],
                                                   short_name=organisation_data['short_name'],
                                                   ogrn=organisation_data['ogrn'],
                                                   inn=organisation_data['inn'],
                                                   kpp=organisation_data['kpp'],
                                                   data_registration=organisation_data['data_registration'],
                                                   chef=organisation_data['chef'],
                                                   contact=organisation_data['contact'],
                                                   target=organisation_data['target'],
                                                   address=object_address
                                                   )
        user = User.objects.create(first_name=user_data['first_name'],
                                   last_name=user_data['last_name'],
                                   email=user_data['email'],
                                   username=user_data['username'],
                                   )
        user.set_password(user_data['password'])
        user.save()
        profile = Profile.objects.create(user=user, organisation=organisation,
                                         phone=validated_data['phone'],
                                         )
        return profile

