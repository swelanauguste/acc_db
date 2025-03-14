from django import forms

from .models import AffidavitNew, Comment


class AffidavitForm(forms.ModelForm):
    class Meta:
        model = AffidavitNew
        fields = "__all__"
        exclude = [
            "affidavit_id",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "slug",
        ]

        widgets = {
            "date_received": forms.DateInput(attrs={"type": "date"}),
            "date_required": forms.DateInput(attrs={"type": "date"}),
            "dob": forms.DateInput(attrs={"type": "date"}),
            "address": forms.Textarea(attrs={"rows": "3"}),
            "comments": forms.Textarea(attrs={"rows": "3"}),
            # "attachment": forms.FileInput(attrs={"accept": "image/*"}),
        }


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comments"]
        widgets = {
            "comments": forms.Textarea(attrs={"rows": "3"}),
        }
