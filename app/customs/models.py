# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customs(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    date_received = models.TextField(db_column='DATE RECEIVED', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    letter_dated = models.TextField(db_column='LETTER DATED', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    from_field = models.TextField(db_column='FROM', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    subject = models.TextField(db_column='SUBJECT', blank=True, null=True)  # Field name made lowercase.
    chassis_no = models.TextField(db_column='CHASSIS NO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vehcile_model = models.TextField(db_column='VEHCILE MODEL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    registration_no = models.TextField(db_column='REGISTRATION NO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    owner_purchaser = models.TextField(db_column='OWNER / PURCHASER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customs'
