from django.urls import path

from . import views

urlpatterns = [
    path("", views.BookRecordsListView.as_view(), name="book-records-list"),
    path(
        "<int:pk>/", views.BookRecordsDetailView.as_view(), name="book-records-detail"
    ),
]
