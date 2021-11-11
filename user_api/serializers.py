from rest_framework import fields, serializers

from api.models import *


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        label= ("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super(RegisterSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user