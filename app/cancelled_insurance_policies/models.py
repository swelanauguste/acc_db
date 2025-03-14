# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CancelledInsurancePolicies(models.Model):
    reference = models.IntegerField(db_column='REFERENCE', blank=True, null=True)  # Field name made lowercase.
    date_received = models.TextField(db_column='Date received', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    letter_dated = models.TextField(db_column='Letter Dated', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_agency_s_name = models.TextField(db_column="Insurance Agency's  Name", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subject = models.TextField(blank=True, null=True)
    policy_holder = models.TextField(db_column='Policy Holder', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    policy_cancellation_date_mm_dd_yy_field = models.TextField(db_column='Policy cancellation date   (mm/dd/yy)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    policy_number = models.TextField(db_column='Policy Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.IntegerField(blank=True, null=True)
    status_date = models.TextField(db_column='status date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    notes = models.TextField(blank=True, null=True)
    file_location = models.TextField(db_column='file location', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    scanned_document = models.IntegerField(db_column='scanned document', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'cancelled_insurance_policies'
