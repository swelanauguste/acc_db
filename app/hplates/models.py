# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Hplates(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    date_received = models.TextField(db_column='DATE RECEIVED', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    applicant_s_name = models.TextField(db_column="APPLICANT'S NAME", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    primary_contact_number = models.FloatField(db_column='PRIMARY CONTACT NUMBER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    registration_number = models.TextField(db_column='REGISTRATION NUMBER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vehicle_model_man = models.TextField(db_column='VEHICLE  MODEL/ MAN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chassis_vin_number = models.TextField(db_column='CHASSIS VIN NUMBER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    action_taken = models.TextField(db_column='ACTION TAKEN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.TextField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    attachments = models.IntegerField(db_column='ATTACHMENTS', blank=True, null=True)  # Field name made lowercase.
    new_aplication = models.IntegerField(db_column='NEW APLICATION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    secondary_contact = models.TextField(db_column='SECONDARY  CONTACT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    continued_use = models.IntegerField(db_column='CONTINUED USE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'hplates'
