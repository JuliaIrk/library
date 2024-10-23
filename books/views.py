from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.

class UnitListView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    # queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"

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
    
    # def put(self, request, *args, **kwargs):
    #     try:
    #         return super().put(request, *args, **kwargs)
    #     except Exception as e:
    #         print(f"{e}")
    
    def get_queryset(self):
        return Book.objects.all()
    
    # def get_object(self):
    #     return Book.objects.get(id=self.kwargs["id"])
    
    # def put(self, request, id:int): #обновление
    #     book = get_object_or_404(Book, id=id)
    #     serializer = BookSerializer(book, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)    

    def delete(self, request, id:int):
        book = get_object_or_404(Book, id=id)
        book.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
