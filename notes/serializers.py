from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User



class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at','owner') 
        # Making owner read-only ensures clients cannot set it manually in requests — you control it from the server.
        # owner should be read-only, assigned automatically


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']
    
    def validate_username(self, value):
        if User.objects.filter(username=value).exists(): # Check if there is already a user in the DB whose username is equal to value
            raise serializers.ValidationError("Username is already taken")
        return value
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )     
        return user                                        
             


