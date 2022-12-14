from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        extra_kwargs = {'password':
                                {'write_only': True}
        }

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user_obj = User(
            username=username,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField()


    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token'
        ]
        extra_kwargs = {'password':
                                {'write_only': True}
        }

    def validate(self, data):
        return data