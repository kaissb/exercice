from django.contrib.auth.models import User
from rest_framework import serializers
from noteapp.models import Note



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')
    def createUser(self,validated_data):
        username = validated_data('username')
        password = validated_data('password')
        user = User.objects.create(
            username = username,
            password = password
        )

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


