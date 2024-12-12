from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Post, Like
from notifications.models import Notification

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Generate a notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked",
                target=post
            )
            return Response({'message': 'Post liked successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        like = Like.objects.filter(user=request.user, post=post)
        if like.exists():
            like.delete()
            return Response({'message': 'Post unliked successfully'}, status=status.HTTP_200_OK)

        return Response({'message': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        followed_users = user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)

class PostViewSet(viewsets.ModelViewSet):
    ...
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

"Post.objects.filter(author__in=following_users).order_by"  
"generics.get_object_or_404(Post, pk=pk)"      
