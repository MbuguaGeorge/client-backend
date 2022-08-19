from user_profile.models import User
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'phone')
    
    def save(self):
        user = User(
            email = self.validated_data['email'],
            name = self.validated_data['name'],
            phone = self.validated_data['phone'],
        )

        password = self.validated_data['password']

        user.set_password(password)
        user.save()
        return user