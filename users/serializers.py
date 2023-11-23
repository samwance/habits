from rest_framework import serializers
from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        user = User.objects.create(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('email', 'password',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
