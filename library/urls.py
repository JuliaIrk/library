from books import views
from django.urls import path, re_path

urlpatterns = [
    # path('',  views.UnitListView.as_view()),
    # re_path(r"book/$", views.UnitListView.as_view()),
    re_path(r"book/(?P<id>\d+)/$", views.UnitListView.as_view()),
]
