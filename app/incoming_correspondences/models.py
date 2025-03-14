# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class IncomingCorrespondences(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    date_received = models.TextField(db_column='Date Received', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    from_field = models.TextField(db_column='From', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    originaly_from = models.TextField(db_column='ORIGINALY FROM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact = models.TextField(blank=True, null=True)
    letter_dated = models.TextField(db_column='Letter Dated', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subject = models.TextField(db_column='Subject', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    email_format = models.IntegerField(db_column='email format', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    file_location = models.TextField(db_column='FILE LOCATION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.TextField(db_column='EMAIL', blank=True, null=True)  # Field name made lowercase.
    attachements = models.IntegerField(db_column='ATTACHEMENTS', blank=True, null=True)  # Field name made lowercase.
    status_date = models.TextField(db_column='STATUS DATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    letter_format = models.IntegerField(db_column='letter format', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'incoming_correspondences'
