from books import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index),
    re_path(r"book/(?P<id>\d+)/$", views.UnitListView.as_view()),
]
