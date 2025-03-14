# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class OutgoingCorrespondences(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    addressee = models.TextField(db_column='ADDRESSEE', blank=True, null=True)  # Field name made lowercase.
    subject = models.TextField(db_column='SUBJECT', blank=True, null=True)  # Field name made lowercase.
    date_dispatched = models.TextField(db_column='DATE DISPATCHED', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_method = models.TextField(db_column='DELIVERY METHOD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    received_by = models.TextField(db_column='RECEIVED BY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_recieved = models.TextField(db_column='DATE RECIEVED', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    notes = models.TextField(db_column='NOTES', blank=True, null=True)  # Field name made lowercase.
    filing_location = models.TextField(db_column='Filing Location', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'outgoing_correspondences'
