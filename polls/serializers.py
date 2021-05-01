from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Posts
from rest_framework.authtoken.models import Token

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('title', 'image')

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request:
            user = request.user
            userobj=User.objects.get(username=user)
        print(user)
        post = Posts.objects.create(**validated_data)
        userobj.posts_set.add(post)
        post.save()
        return post

