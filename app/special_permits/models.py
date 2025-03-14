# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SpecialPermits(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    applicant = models.TextField(db_column='APPLICANT', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    veh_registration = models.IntegerField(db_column='VEH REGISTRATION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address = models.TextField(db_column='ADDRESS', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    decision = models.TextField(db_column='DECISION', blank=True, null=True)  # Field name made lowercase.
    issue_date = models.TextField(db_column='ISSUE DATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    expiry_date = models.TextField(db_column='EXPIRY DATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    file_location = models.TextField(db_column='FILE LOCATION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    attachment = models.FloatField(db_column='ATTACHMENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'special_permits'
