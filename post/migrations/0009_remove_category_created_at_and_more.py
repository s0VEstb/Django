# Generated by Django 5.0.2 on 2024-02-17 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_remove_review_post_review_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated_at',
        ),
    ]