from rest_framework import serializers
from api import models


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.UserProfile
        fields=('id','email','first_name','last_name','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self,validated_data):
        user=models.UserProfile.objects.create_user(email=validated_data['email'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],password=validated_data['password'])
        return user

    def update(self,instance,validated_data):
        if 'password' in validated_data:
            password=validated_data['password']
            instance.set_password(password)
        return super().update(instance,validated_data)