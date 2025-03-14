# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import random
import string

from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from users.models import User


class Affidavits(models.Model):
    id = models.IntegerField(
        db_column="ID", blank=True, primary_key=True
    )  # Field name made lowercase.
    date_received = models.TextField(
        db_column="DATE RECEIVED", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_required = models.TextField(
        db_column="DATE REQUIRED", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    officer_name = models.TextField(
        db_column="OFFICER NAME", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_number = models.TextField(
        db_column="CONTACT NUMBER", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    licence_name = models.TextField(
        db_column="LICENCE NAME", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dob = models.TextField(
        db_column="DOB", blank=True, null=True
    )  # Field name made lowercase.
    adress = models.TextField(
        db_column="ADRESS", blank=True, null=True
    )  # Field name made lowercase.
    vehicle_number = models.TextField(
        db_column="VEHICLE NUMBER", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vehicle_owner = models.TextField(
        db_column="VEHICLE OWNER", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mand = models.TextField(
        db_column="MAND", blank=True, null=True
    )  # Field name made lowercase.
    colour = models.TextField(
        db_column="COLOUR", blank=True, null=True
    )  # Field name made lowercase.
    chassis_number = models.TextField(
        db_column="CHASSIS NUMBER", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    engine_number = models.TextField(
        db_column="ENGINE NUMBER", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(
        db_column="STATUS", blank=True, null=True
    )  # Field name made lowercase.
    status_date = models.TextField(
        db_column="STATUS DATE", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comments = models.TextField(
        db_column="COMMENTS", blank=True, null=True
    )  # Field name made lowercase.
    licence_number = models.TextField(
        db_column="LICENCE NUMBER", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    attachment = models.IntegerField(
        db_column="ATTACHMENT", blank=True, null=True
    )  # Field name made lowercase.
    type_requested = models.IntegerField(
        db_column="TYPE REQUESTED", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "affidavits"


class RequestType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name.title()


def generate_short_id():
    length = 8  # You can adjust the length as needed
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for i in range(length)).upper()


class AffidavitNew(models.Model):
    affidavit_id = models.CharField(
        default=generate_short_id, editable=False, unique=True, max_length=8
    )
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    date_received = models.DateField()
    date_required = models.DateField()
    officer_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    request_type = models.ForeignKey(
        RequestType,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="affidavit_request_types",
    )
    licence_name = models.CharField(max_length=255, blank=True)
    licence_number = models.CharField(max_length=255, blank=True)
    dob = models.DateField("D.O.B", blank=True)
    address = models.TextField()
    vehicle_owner = models.CharField(max_length=255, blank=True)
    vehicle_number = models.CharField(max_length=255, blank=True)
    maker = models.CharField(max_length=255, blank=True)
    chassis_number = models.CharField(max_length=255, blank=True)
    engine_number = models.CharField(max_length=255, blank=True)
    colour = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)
    attachment = models.FileField(blank=True, upload_to="affidavit_new/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="affidavit_new_created_by"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="affidavit_new_updated_by"
    )
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.affidavit_id)
        super(AffidavitNew, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("affidavit-new-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.affidavit_id}"


class Status(models.Model):
    affidavit = models.ForeignKey(
        AffidavitNew, on_delete=models.CASCADE, related_name="statuses"
    )
    status = models.CharField(max_length=255)
    date = models.DateField()
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="status_created_by"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="status_updated_by"
    )

    def __str__(self):
        return f"{self.affidavit.affidavit_id} {self.status}"


class Comment(models.Model):
    affidavit = models.ForeignKey(
        AffidavitNew, on_delete=models.CASCADE, related_name="affidavit_comments"
    )
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="affidavit_created_by"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="affidavit_updated_by"
    )
    
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.affidavit} {self.comment[:20]}"
