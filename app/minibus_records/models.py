# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MinibusRecords(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    number_plate = models.TextField(db_column='NUMBER PLATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    owners_1st_name = models.TextField(db_column='OWNERS 1ST NAME', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    owners_middle_name = models.TextField(db_column='OWNERS MIDDLE  NAME', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    owners_sir_name = models.TextField(db_column='OWNERS SIR NAME', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sold_to = models.TextField(db_column='SOLD TO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    add_a_name = models.TextField(db_column='ADD A NAME', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    route_name = models.TextField(db_column='ROUTE NAME', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bus_association = models.TextField(db_column='BUS ASSOCIATION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name_of_insurance = models.TextField(db_column='NAME OF INSURANCE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_issue_date = models.TextField(db_column='INSURANCE ISSUE DATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insurance_exp_date = models.TextField(db_column='INSURANCE EXP DATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chassis_number = models.TextField(db_column='CHASSIS NUMBER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    engine_number = models.TextField(db_column='ENGINE NUMBER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    permit_number = models.TextField(db_column='PERMIT NUMBER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    permit_issue_date = models.TextField(db_column='PERMIT ISSUE DATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    permit_expiry_date = models.TextField(db_column='PERMIT EXPIRY DATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    new_permit_issue = models.TextField(db_column='New Permit issue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    new_permit_expiry = models.TextField(db_column='New Permit expiry', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    transaction_completed_date = models.TextField(db_column='TRANSACTION COMPLETED DATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    month = models.TextField(db_column='MONTH', blank=True, null=True)  # Field name made lowercase.
    transaction_year = models.IntegerField(db_column='TRANSACTION YEAR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    transaction_status = models.TextField(db_column='TRANSACTION STATUS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'minibus_records'
