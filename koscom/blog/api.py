import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer


# class PostListView(generics.ListCreateAPIView):

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

'''
post_list = PostListView.as_view({
    'get': 'list',
    'post': 'create',
})
'''

