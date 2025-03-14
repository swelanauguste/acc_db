# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BookRecords(models.Model):
    id = models.IntegerField(
        db_column="ID", blank=True, primary_key=True
    )  # Field name made lowercase.
    date = models.TextField(
        db_column="Date", blank=True, null=True
    )  # Field name made lowercase.
    book_type = models.TextField(
        db_column="BOOK TYPE", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_ordered = models.TextField(
        db_column="DATE ORDERED", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    qty_ordered = models.IntegerField(
        db_column="QTY ORDERED", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    qty_received = models.FloatField(
        db_column="QTY RECEIVED", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_received = models.FloatField(
        db_column="DATE RECEIVED", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    agency_ordered_from = models.TextField(
        db_column="AGENCY ORDERED FROM", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.TextField(
        db_column="EMAIL", blank=True, null=True
    )  # Field name made lowercase.
    attachment = models.IntegerField(
        db_column="ATTACHMENT", blank=True, null=True
    )  # Field name made lowercase.
    status_of_order = models.TextField(
        db_column="STATUS OF ORDER", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status_date = models.TextField(
        db_column="STATUS DATE", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "book_records"
