from re import L
from sys import implementation
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from links.models import Link
from links.serizliers import LinkSerializer
from links.models import Link
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# Create your views here.


class PostListApi(generics.ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostCreateApi(generics.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDetailApi(generics.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostUpdateApi(generics.UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDeleteApi(generics.DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
