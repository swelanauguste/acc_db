from django.urls import path

from . import views

urlpatterns = [
    path("", views.ExemptionListView.as_view(), name="exemption-list"),
    path("home/", views.index, name="home"),
    path("download/", views.download_file, name="download_file"),
    path("export/", views.export_to_sqlite, name="export_to_sqlite"),
    path("h-plates/", views.HPplateListView.as_view(), name="hplate-list"),
    path("hplate/<int:pk>/", views.HPplatesDetailView.as_view(), name="hplate-detail"),
    path(
        "exemption/<int:pk>/",
        views.ExemptionDetailView.as_view(),
        name="exemption-detail",
    ),
]
