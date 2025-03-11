# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class HPlates(models.Model):
    id = models.IntegerField(
        db_column="ID", blank=True, primary_key=True
    )  # Field name made lowercase.
    date_received = models.TextField(
        db_column="DATE RECEIVED", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    applicant_s_name = models.TextField(
        db_column="APPLICANT'S NAME", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    primary_contact_number = models.FloatField(
        db_column="PRIMARY CONTACT NUMBER", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    registration_number = models.TextField(
        db_column="REGISTRATION NUMBER", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vehicle_model_man = models.TextField(
        db_column="VEHICLE  MODEL/ MAN", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chassis_vin_number = models.TextField(
        db_column="CHASSIS VIN NUMBER", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    action_taken = models.TextField(
        db_column="ACTION TAKEN", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.TextField(
        db_column="DATE", blank=True, null=True
    )  # Field name made lowercase.
    status = models.TextField(
        db_column="STATUS", blank=True, null=True
    )  # Field name made lowercase.
    attachments = models.IntegerField(
        db_column="ATTACHMENTS", blank=True, null=True
    )  # Field name made lowercase.
    new_aplication = models.IntegerField(
        db_column="NEW APLICATION", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    secondary_contact = models.TextField(
        db_column="SECONDARY  CONTACT", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    continued_use = models.IntegerField(
        db_column="CONTINUED USE", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "hplates"
        ordering = ["date_received"]


class Exemptions(models.Model):
    id = models.IntegerField(
        db_column="ID", blank=True, primary_key=True
    )  # Field name made lowercase.
    name_of_applicant = models.TextField(
        db_column="NAME OF APPLICANT", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_received = models.TextField(
        db_column="DATE RECEIVED", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type_of_exemption = models.TextField(
        db_column="TYPE OF EXEMPTION", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    telephone_no_1 = models.TextField(
        db_column="TELEPHONE NO 1", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    telephone_no_2 = models.TextField(
        db_column="TELEPHONE NO 2", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.TextField(
        db_column="EMAIL", blank=True, null=True
    )  # Field name made lowercase.
    amount_to_be_paid = models.FloatField(
        db_column="AMOUNT TO BE PAID", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status_1 = models.TextField(
        db_column="STATUS 1", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comments = models.TextField(
        db_column="COMMENTS", blank=True, null=True
    )  # Field name made lowercase.
    date_of_status_update = models.TextField(
        db_column="DATE  OF STATUS UPDATE", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    notes = models.TextField(
        db_column="NOTES", blank=True, null=True
    )  # Field name made lowercase.
    decision = models.TextField(
        db_column="DECISION", blank=True, null=True
    )  # Field name made lowercase.
    attachment = models.IntegerField(
        db_column="ATTACHMENT", blank=True, null=True
    )  # Field name made lowercase.
    status_2 = models.TextField(
        db_column="STATUS 2", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    castries = models.IntegerField(
        db_column="CASTRIES", blank=True, null=True
    )  # Field name made lowercase.
    vieux_fort = models.IntegerField(
        db_column="VIEUX FORT", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "exemptions"
        ordering = ["-date_received"]
