from itertools import chain

from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import AffidavitForm
from .models import AffidavitNew, Affidavits


class AffidavitNewListView(ListView):
    model = AffidavitNew


class AffidavitNewDetailView(DetailView):
    model = AffidavitNew


class AffidavitCreateView(CreateView):
    model = AffidavitNew
    form_class = AffidavitForm


class AffidavitUpdateView(UpdateView):
    model = AffidavitNew
    form_class = AffidavitForm


class AffidavitsListView(ListView):
    model = Affidavits


class AffidavitsDetailView(DetailView):
    model = Affidavits
