
from django.urls import include, path
from polls import views
from rest_framework.authtoken.views import obtain_auth_token

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('create-user/', views.UserCreate.as_view()),
    path('add-post/',views.createPost.as_view()),
    path('posts/',views.createPostNew.as_view())
    
]
