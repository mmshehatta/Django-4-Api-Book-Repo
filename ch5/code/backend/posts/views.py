# posts/views.py
from rest_framework import generics, permissions # new
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly # new



class PostList(generics.ListCreateAPIView):
	# permission_classes = (permissions.IsAuthenticated,) # new
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	# permission_classes = (permissions.IsAuthenticated,) # new
	permission_classes = (IsAuthorOrReadOnly,) # new
	queryset = Post.objects.all()
	serializer_class = PostSerializer