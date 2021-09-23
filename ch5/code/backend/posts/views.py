# posts/views.py
from rest_framework import generics, permissions # new
from .models import Post
from .serializers import PostSerializer, UserSerializer # new
from .permissions import IsAuthorOrReadOnly # new
from django.contrib.auth import get_user_model # new
from rest_framework import viewsets # new




# class PostList(generics.ListCreateAPIView):
# 	# permission_classes = (permissions.IsAuthenticated,) # new
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
# 	# permission_classes = (permissions.IsAuthenticated,) # new
# 	permission_classes = (IsAuthorOrReadOnly,) # new
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer


class PostViewSet(viewsets.ModelViewSet): # new
	permission_classes = (IsAuthorOrReadOnly,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer


# class UserList(generics.ListCreateAPIView): # new
# 	queryset = get_user_model().objects.all()
# 	serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
# 	queryset = get_user_model().objects.all()
# 	serializer_class = UserSerializer	


class UserViewSet(viewsets.ModelViewSet): # new
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
