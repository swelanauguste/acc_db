from itertools import chain

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.db.models import Q
from .forms import AffidavitForm
from .models import AffidavitNew, Affidavits


class AffidavitNewListView(LoginRequiredMixin, ListView):
    model = AffidavitNew


class AffidavitNewDetailView(LoginRequiredMixin, DetailView):
    model = AffidavitNew


class AffidavitCreateView(LoginRequiredMixin, CreateView):
    model = AffidavitNew
    form_class = AffidavitForm


class AffidavitUpdateView(LoginRequiredMixin, UpdateView):
    model = AffidavitNew
    form_class = AffidavitForm


class AffidavitsListView(LoginRequiredMixin, ListView):
    model = Affidavits


class AffidavitsDetailView(LoginRequiredMixin, DetailView):
    model = Affidavits
