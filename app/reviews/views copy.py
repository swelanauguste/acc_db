from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, TemplateView

from .models import Exemptions, HPlates
from .tasks import download_file, export_to_sqlite


def index(request):
    return render(request, "reviews/index.html")


def update_database(request):
    download_file(request)
    export_to_sqlite()
    return redirect("/")


class HPplateListView(ListView):
    model = HPlates
    # paginate_by = 20


class HPplatesDetailView(DetailView):
    model = HPlates


class ExemptionListView(ListView):
    model = Exemptions
    # paginate_by = 100


class ExemptionDetailView(DetailView):
    model = Exemptions
