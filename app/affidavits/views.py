from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import AffidavitForm, CommentCreateForm
from .models import AffidavitNew, Affidavits


class AffidavitNewListView(LoginRequiredMixin, ListView):
    model = AffidavitNew


class AffidavitNewDetailView(LoginRequiredMixin, DetailView):
    model = AffidavitNew
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentCreateForm
        return context
    

@login_required
def add_comment_view(request, slug):
    affidavit = get_object_or_404(AffidavitNew, slug=slug)
    print(affidavit)
    form = CommentCreateForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            comment = form.save(commit=False)
            comment.affidavit = affidavit
            if request.user.is_authenticated:
                comment.created_by = request.user
                comment.updated_by = request.user
            comment.save()
            return redirect("affidavit-new-detail", slug=slug)

    # If the form is not valid or the request method is not POST
    return render(
        request,
        "affidavits/affidavitnew_detail.html",
        {"object": affidavits, "form": form},
    )


class AffidavitCreateView(LoginRequiredMixin, CreateView):
    model = AffidavitNew
    form_class = AffidavitForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class AffidavitUpdateView(LoginRequiredMixin, UpdateView):
    model = AffidavitNew
    form_class = AffidavitForm

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class AffidavitsListView(LoginRequiredMixin, ListView):
    model = Affidavits


class AffidavitsDetailView(LoginRequiredMixin, DetailView):
    model = Affidavits
    
    


