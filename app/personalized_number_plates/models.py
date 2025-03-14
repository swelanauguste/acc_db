# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PersonalizedNumberPlates(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    applicant_name = models.TextField(db_column='APPLICANT NAME', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address = models.TextField(db_column='ADDRESS', blank=True, null=True)  # Field name made lowercase.
    personalized = models.TextField(db_column='PERSONALIZED', blank=True, null=True)  # Field name made lowercase.
    vehcle_type = models.TextField(db_column='VEHCLE TYPE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vehicle_no = models.TextField(db_column='VEHICLE NO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    telephone_field = models.TextField(db_column='TELEPHONE #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    email = models.TextField(db_column='EMAIL', blank=True, null=True)  # Field name made lowercase.
    date_dispatched_to_roc = models.TextField(db_column='DATE DISPATCHED TO RoC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='NOTES', blank=True, null=True)  # Field name made lowercase.
    attachment = models.IntegerField(db_column='ATTACHMENT', blank=True, null=True)  # Field name made lowercase.
    letter_prepared = models.IntegerField(db_column='LETTER PREPARED', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'personalized_number_plates'
