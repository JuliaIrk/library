from books import views
from django.urls import path, re_path

urlpatterns = [
    # path('',  views.UnitListView.as_view()),
    # re_path(r"book/$", views.UnitListView.as_view()),
    path('books/', views.BookList.as_view(), name='book-list'),
    path('users/', views.UserList.as_view(), name='user-list'),
    # path('loans/', LoanList.as_view(), name='loan-list'),
    # path('bookonhand/', BooksOnHand.as_view(), name='book-on-hand-list'),
    # path('outstanding/', Outstabding.as_view(), name='outstanding-list'),
    re_path(r"book/(?P<id>\d+)/$", views.UnitListView.as_view()),
]
