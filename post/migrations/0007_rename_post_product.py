# Generated by Django 5.0.2 on 2024-02-16 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_rename_product_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Product',
        ),
    ]