from user_profile.models import User
from rest_framework import serializers
from django.contrib.auth.tokens import default_token_generator

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'phone', 'email_token')
    
    def save(self):
        user = User(
            email = self.validated_data['email'],
            name = self.validated_data['name'],
            phone = self.validated_data['phone'],
        )
        confirmation_Token = default_token_generator.make_token(user)
        password = self.validated_data['password']

        user.email_token=confirmation_Token
        user.set_password(password)
        user.save()
        return user