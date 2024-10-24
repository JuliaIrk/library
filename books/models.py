from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    isbn = models.CharField(max_length=50)
    available_copies = models.IntegerField(default=1)

    def _str_(self):
        return self.title

class Reader(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def _str_(self):
        return self.name
    
class Loan(models.Model): #задолженность
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    user = models.ForeignKey(Reader, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)#Дата, когда книгу взяли
    return_due_date = models.DateField()# дата, когда книгу нужно вернуть
    returned_date = models.DateField(null=True, blank=True)#фактическая дата возврата