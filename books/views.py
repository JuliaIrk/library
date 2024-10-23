from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.
def index(request):
    return HttpResponse("Главная")

class UnitListView(generics.ListAPIView):
    
    serializer_class = BookSerializer

    def get(self, request, id:int):
        queryset = Book.objects.filter(id=id)
        serializer = self.get_serializer(queryset, many = True)

        return Response(serializer.data, status=status.HTTP_200_OK)