# Generated by Django 2.2.6 on 2019-11-02 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customermanage', '0002_auto_20191102_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase_order',
            old_name='Purchase_number',
            new_name='Customer_number',
        ),
    ]