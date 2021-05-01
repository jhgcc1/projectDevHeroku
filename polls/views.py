from django.contrib.auth.models import User
from rest_framework import generics
from polls.serializers import UsersSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from polls.models import Posts
from rest_framework.permissions import IsAuthenticated
class createPost(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    def post(self, request):
        try:
            title = request.data['title']
            user= request.user
            post = Posts.objects.create(user=user,title=title)
            return Response({"success":"post created"})
        except:
            return Response({"error": "error creating post"})
    def get(self, request):
        user= request.user
        posts=Posts.objects.get(user=user)
        print(posts)
        return Response(posts)
        
class UserCreate(generics.CreateAPIView):
    serializer_class = UsersSerializer
    permission_classes = (AllowAny, )

class createPostNew(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = PostSerializer
    def get_queryset(self):
        user = self.request.user
        return Posts.objects.filter(user=user)





