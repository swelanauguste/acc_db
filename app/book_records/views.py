from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import BookRecords


class BookRecordsListView(LoginRequiredMixin, ListView):
    model = BookRecords


class BookRecordsDetailView(LoginRequiredMixin, DetailView):
    model = BookRecords
