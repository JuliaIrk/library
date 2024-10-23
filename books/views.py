from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.

class UnitListView(generics.ListAPIView, generics.CreateAPIView):
    
    serializer_class = BookSerializer

    def get(self, request): #Получение список всех книг (GET)
        author = request.GET.get("author")
        published_date = request.GET.get("date")
        if author:
            queryset = Book.objects.filter(author=author)
            # serializer = BookSerializer(queryset.first())
        elif published_date:
            queryset = Book.objects.filter(published_date=published_date)
        else:
            queryset = Book.objects.all()
        
        serializer = self.get_serializer(queryset, many = True)    
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)