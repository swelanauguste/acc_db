# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class InvoicesPayments(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    date_recorded = models.TextField(db_column='Date recorded', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    company = models.TextField(blank=True, null=True)
    quotation_amount_if_applicable_field = models.TextField(db_column='quotation amount (if applicable)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    quotation_date = models.TextField(db_column='Quotation Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    requisition_date_if_applicable_field = models.TextField(db_column='Requisition  Date ( if applicable)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    purchase_order_date = models.TextField(db_column='Purchase Order date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    purchase_order_field = models.TextField(db_column='Purchase Order #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    item_was_ordered_field = models.TextField(db_column='Item was ordered?', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    good_s_received_field = models.TextField(db_column='Good(s) received?', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    invoice_field = models.TextField(db_column='Invoice #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    invoice_date = models.TextField(db_column='Invoice Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    invcoice_sent_to_accounts = models.TextField(db_column='invcoice sent to accounts', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    date_sent_to_accounts = models.TextField(db_column='date sent to accounts', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    file_location = models.TextField(db_column='File Location', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invoices_payments'
