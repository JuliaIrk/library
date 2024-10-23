from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta():
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'isbn']

def create(self, validated_data):
    return Book.objects.create(**validated_data)

def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.author = validated_data.get('author', instance.author)
    instance.published_date = validated_data.get('published_date', instance.published_date)
    instance.isbn = validated_data.get('isbn', instance.isbn)


