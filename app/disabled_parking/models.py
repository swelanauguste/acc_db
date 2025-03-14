# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DisabledParking(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    date_of_application = models.TextField(db_column='DATE OF APPLICATION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    applicant_name = models.TextField(db_column='APPLICANT NAME', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address = models.TextField(db_column='ADDRESS', blank=True, null=True)  # Field name made lowercase.
    contact_number_1 = models.IntegerField(db_column='CONTACT NUMBER 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_number = models.IntegerField(db_column='CONTACT NUMBER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email_address = models.TextField(db_column='EMAIL ADDRESS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    type_of_permit_granted = models.TextField(db_column='TYPE OF PERMIT GRANTED', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_if_temporary_start_date = models.TextField(db_column='(if temporary) START DATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_if_temporary_end_date = models.TextField(db_column='(if temporary) END DATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    comments = models.TextField(db_column='COMMENTS', blank=True, null=True)  # Field name made lowercase.
    file_location = models.TextField(db_column='FILE LOCATION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    approval_status = models.TextField(db_column='APPROVAL STATUS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    applicant_drive_self = models.IntegerField(db_column='APPLICANT DRIVE SELF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    driver_s_name_if_not_self_field = models.FloatField(db_column="DRIVER'S NAME ( IF NOT SELF )", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    drivers_licence = models.TextField(db_column='DRIVERS LICENCE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    medical_condition = models.TextField(db_column='MEDICAL CONDITION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    doctor_s_name = models.TextField(db_column="DOCTOR'S NAME", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    new_issue = models.IntegerField(db_column='NEW ISSUE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    replacement = models.IntegerField(db_column='REPLACEMENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disabled_parking'
