from django.urls import path

from . import views

urlpatterns = [
    path("", views.AffidavitsListView.as_view(), name="affidavits-list"),
    path(
        "affidavits/<int:pk>/",
        views.AffidavitsDetailView.as_view(),
        name="affidavits-detail",
    ),
    path("new/", views.AffidavitNewListView.as_view(), name="affidavit-new-list"),
    path("new/create/", views.AffidavitCreateView.as_view(), name="affidavit-create"),
    path(
        "affidavit-new/<slug:slug>/",
        views.AffidavitNewDetailView.as_view(),
        name="affidavit-new-detail",
    ),
    path(
        "affidavit-update/<slug:slug>/",
        views.AffidavitUpdateView.as_view(),
        name="affidavit-new-update",
    ),
    path(
        "affidavit-add-comment/<slug:slug>/",
        views.add_comment_view,
        name="affidavit-add-comment",
    )
]
